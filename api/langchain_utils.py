from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


qa_prompt = PromptTemplate.from_template(
    "Answer on {input}. Previous dialog history is {chat_history}"
)

def get_rag_chain(model="llama3.2"):
    llm = ChatOllama(model=model)
    rag_chain = qa_prompt | llm | StrOutputParser()
    return rag_chain

