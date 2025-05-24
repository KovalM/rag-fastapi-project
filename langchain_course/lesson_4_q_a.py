from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import DocArrayInMemorySearch
# from IPython.display import display, Markdown
from langchain.indexes import VectorstoreIndexCreator



llm = ChatOllama(temperature=0.0, model="llama3.2")

file = 'langchain_course/Data.csv'
loader = CSVLoader(file_path=file)

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

index = VectorstoreIndexCreator(
    embedding=embedding,
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])

query ="What is EcoBrew Reusable Coffee Cup?"

print(index.query(query, llm=llm))



