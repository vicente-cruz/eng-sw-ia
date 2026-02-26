from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import chain
from dotenv import load_dotenv

load_dotenv()

@chain
def square(input_dict:dict) -> dict:
    x = input_dict["x"]
    return {"square_result": x * x}

question_template01 = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a joke with my name!"
)

question_template02 = PromptTemplate(
    input_variables=["square_result"],
    template="Tell me about the number {square_result}"
)

model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

chain01 = question_template01 | model
chain02 = square | question_template02 | model

# result = chain01.invoke({"name": "Vicente"})
result = chain02.invoke({"x": 5})
print(result.content)