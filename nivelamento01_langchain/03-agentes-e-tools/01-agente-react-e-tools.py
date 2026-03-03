from langchain.tools import tool
from langchain_openai import ChatOpenAI
# Deprecated: versoes 0.X LangChain
# from langchain.agents import create_react_agent, AgentExecutor
# from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
# Para puxar do hub
from langsmith import Client
from dotenv import load_dotenv

load_dotenv()

@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
    """Evaluate a simple mathematical expression and returns the result."""
    try:
        result = eval(expression) # Be careful with this because it's a security risk
    except Exception as e:
        return f"Error: {e}"

    return str(result)

@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """Mocked web search tool. Returns a hardcoded result."""

    data = {
        "Brazil": "Brasília",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United States": "Washington, D.C.",
    }
    for country, capital in data.items():
        if country.lower() in query.lower():
            return f"The capital of {country} is {capital}"
    return "I don't know the capital of that country."

llm = ChatOpenAI(model="gpt-5-mini", disable_streaming=True)

tools = [calculator, web_search_mock]

# Deprecated: versoes 0.X do LangChain
# prompt = PromptTemplate.from_template(
SYSTEM_PROMPT = """
Answer the following questions as best you can. You have access to the following tools.
Only use the information you get from the tools, even if you know the answer.
If the information is not provided by the tools, say you don't know.

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action

... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Rules:
- If you choose an Action, do NOT include Final Answer in the same step.
- After Action and Action Input, stop and wait for Observation.
- Never search the internet. Only use the tools provided.

Begin!

Question: {input}
Thought:{agent_scratchpad}"""
# )

# Deprecated: versoes 0.X do LangChain
# agent_chain = create_react_agent(llm, tools, prompt, stop_sequence=False)

client = Client()
PROMPT_HUB = client.pull_prompt("hwchase17/react")

agent = create_agent(
    model=llm,
    tools=tools,
    # system_prompt=SYSTEM_PROMPT
    system_prompt=PROMPT_HUB.template
)

# Deprecated: versoes 0.X do LangChain
# agent_executor = AgentExecutor.from_agent_and_toos(
#     agent=agent_chain,
#     tools=tools,
#     verbose=True,
#     handle_parsing_errors=True,
#     max_iterations=3
# )

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the capital of Iran?"
                # "content": "How much is 10 + 10?"
            }
        ]
    }
)

# Deprecated: versoes 0.X do LangChain
# print(agent_executor.invoke({"input": "How much is 10 + 10?"}))
print(result["messages"][-1].content)