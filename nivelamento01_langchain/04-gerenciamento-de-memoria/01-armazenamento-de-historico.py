from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv()

# Criação do Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Criação do Modelo
chat_model = ChatOpenAI(model="gpt-5-nano", temperature=0.9)

# Criação do Chain Básico
chain = prompt | chat_model

# GERENCIAMENTO DE SESSÃO
session_store: dict[str, InMemoryChatMessageHistory] = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

# Crianção do Chain no Histórico
conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "demo-session"}}

response01 = conversational_chain.invoke(
    {"input": "Hello! My name is Vicente. How are you?"},
    config=config
)
print("Assistant: ", response01.content)
print("-"*30)

response02 = conversational_chain.invoke(
    {"input": "can you repeat my name?"},
    config=config
)
print("Assistant: ", response02.content)
print("-"*30)

response03 = conversational_chain.invoke(
    {"input": "Can you repeat my name in a motivation phrase?"},
    config=config
)
print("Assistant: ", response03.content)
print("-"*30)