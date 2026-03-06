from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Executar o script dentro da pasta em que o arquivo está:
# $ cd 05-loaders-e-banco-de-dados-vetoriais
# $ python 02-carregamento-de-pdf.py
loader = PyPDFLoader("gpt5.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks = splitter.split_documents(docs)

for chunk in chunks:
    print("=======================================")
    print(chunk)
    print("=======================================")

print(f"Total de chunks: {len(chunks)}")