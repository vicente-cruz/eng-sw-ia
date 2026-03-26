from langchain_openai import ChatOpenAI
from utils import print_llm_result
from dotenv import load_dotenv
load_dotenv()

msg1 = """
Question: In an API endpoint that returns a list of users and their posts, the developer wrote:

users := db.FindAllUsers()
for _, u := range users {
    u.Posts := db.FindPostsByUserID(u.ID)

How many database queries will this code execute if there are N users?

Generate 3 differents reasoning paths step by step.
At the end, summarize the answer and choose the most consistent one, ignoring outliers.
If there are 3 different answers, ONLY reply: "I can't find a consistent answer".
"""

# llm = ChatOpenAI(model="gpt-3.5-turbo")
# llm = ChatOpenAI(model="gpt-4o")
llm = ChatOpenAI(model="gpt-5-nano")
response1 = llm.invoke(msg1)

print_llm_result(msg1, response1)