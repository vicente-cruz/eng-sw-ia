from langchain_openai import ChatOpenAI
from utils import print_llm_result
from dotenv import load_dotenv
load_dotenv()

msg1 = """
Classify the log severity.

Input: "Disk usage at 85%."
Answer only with ERROR, WARNING, or INFO.
"""

msg2 = """
Classify the log severity.

Input: "Disk usage at 85%."
Think step by step about why this is ERROR, WARNING, or INFO.
At the end, give only the final answer after "Answer:".
"""

msg3 = """
Question: How many "r" are in the word "strawberry"?
Answer only with the number of "r".
"""

msg4 = """
Question: How many "r" are in the word "strawberry"?
Explain step by step by breking down each letter in bullet points, pointing out the "r" before giving the final answer.
"""

# llm = ChatOpenAI(model="gpt-3.5-turbo")
# llm = ChatOpenAI(model="gpt-4o")
llm = ChatOpenAI(model="gpt-5-nano")
response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)
response4 = llm.invoke(msg4)


print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)
print_llm_result(msg4, response4)