from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_classic.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()

long_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in quam eu nunc ornare mattis vitae vel lorem. In hac habitasse platea dictumst. Mauris id feugiat nisl. Praesent eget erat id mauris dapibus lobortis. Proin vulputate scelerisque felis, nec aliquam urna interdum non. Pellentesque non felis bibendum neque pulvinar pretium. Donec consequat fermentum congue. Nullam luctus, purus sed fringilla ullamcorper, metus leo lacinia enim, vel convallis velit odio id nunc. Aenean et pulvinar nisl. Praesent semper fermentum magna non mattis. Integer fermentum pretium magna, in lacinia enim ultricies non.

Nunc vel lacus fermentum, tincidunt dui sit amet, consequat tellus. Suspendisse potenti. Aenean vel vehicula erat, eget lacinia nulla. Aliquam lobortis at ligula non lacinia. Quisque dignissim blandit finibus. Cras ut felis metus. Nulla id accumsan lacus, eget imperdiet est. Nam sem urna, consectetur sit amet facilisis sit amet, scelerisque et tellus. Nunc tristique semper lectus ac suscipit. Donec cursus ultrices augue. Maecenas ultricies malesuada tincidunt. Cras urna risus, venenatis ut aliquam congue, imperdiet eget nunc. Sed vitae felis suscipit, dignissim elit a, convallis ex. Integer laoreet pharetra libero a cursus.

Quisque accumsan elementum metus. Quisque lorem lectus, hendrerit sit amet ornare sed, laoreet id magna. Pellentesque lobortis nisi sit amet tincidunt ullamcorper. Nulla id ligula eget sem bibendum cursus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Quisque feugiat sodales tellus. Cras rhoncus nisi in justo tincidunt suscipit. Aenean non eros libero. Suspendisse auctor sapien vel nunc blandit luctus.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, chunk_overlap=70
)

parts = splitter.create_documents([long_text])

# for part in parts:
#     print(part.page_content)
#     print("-"*30)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

#LCEL map stage: summarize each chunk
map_prompt = PromptTemplate.from_template("Write a concise summary of the following text:\n{context}")
map_chain = map_prompt | llm | StrOutputParser()

prepare_map_inputs = RunnableLambda(lambda docs: [{"context": d.page_content} for d in docs])
map_stage = prepare_map_inputs | map_chain.map()

#LCEL reduce stage: combine summaries into one final summary
reduce_prompt = PromptTemplate.from_template("Combine the following summaries into a single concise summary::\n{context}")
reduce_chain = reduce_prompt | llm | StrOutputParser()

prepare_reduce_input = RunnableLambda(lambda summaries: [{"context": "\n".join(summaries)}])
pipeline = map_stage | prepare_reduce_input | reduce_chain

# chain_sumarize = load_summarize_chain(llm, chain_type="map_reduce", verbose=True)
# chain_sumarize = load_summarize_chain(llm, chain_type="stuff", verbose=False)

result = pipeline.invoke(parts)

print(result)
# print(result["output_text"])