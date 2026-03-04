from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import trim_messages
from langchain_core.runnables import RunnableLambda

load_dotenv()

# Criação do Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a helpful assistant that answers with a short joke when possible."),
    MessagesPlaceholder("history"),
    ("human", "{input}")
])

# Criação do Modelo
llm = ChatOpenAI(model="gpt-5-nano", temperature=0.9)

# Início da implementação da Janela Deslizanter (Sliding Window)
def prepare_inputs(payload: dict) -> dict:
    raw_history = payload.get("raw_history", [])
    trimmed = trim_messages(
        raw_history,
        token_counter=len,
        max_tokens=2,
        strategy="last",
        start_on="human",
        include_system=True,
        allow_partial=False
    )
    return {
        "input": payload.get("input",""),
        "history": trimmed
    }

# Cria a chain com Sliding Window
prepare = RunnableLambda(prepare_inputs)
chain = prepare | prompt | llm

session_store: dict[str, InMemoryChatMessageHistory] = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="raw_history"
)

# Simulação de interação
config = {
    "configurable": {
        "session_id": "demo_session"
    }
}

response01 = conversational_chain.invoke(
    {"input": "My name is Vicente. Reply with a OK, don't mention my name."},
    config=config
)
print("Assistant: ", response01.content)

response02 = conversational_chain.invoke(
    {"input": "Tell me a sentence with a funny fact, don't mention my name."},
    config=config
)
print("Assistant: ", response02.content)

response03 = conversational_chain.invoke(
    {"input": "What is my name?"},
    config=config
)
print("Assistant: ", response03.content)