import re
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import DocArrayInMemorySearch
# from IPython.display import display, Markdown
from langchain.indexes import VectorstoreIndexCreator
from langchain.evaluation.qa import QAGenerateChain
from langchain.evaluation.qa import QAEvalChain
from langchain.output_parsers import RegexParser

llm = ChatOllama(temperature=0.0, model="llama3.2")

file = 'langchain_course/Data.csv'
loader = CSVLoader(file_path=file)
data = loader.load()

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

index = VectorstoreIndexCreator(
    embedding=embedding,
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])

qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=index.vectorstore.as_retriever(), 
    verbose=True,
    chain_type_kwargs = {
        "document_separator": "<<<<>>>>>"
    }
)

regex_parser = RegexParser(
    regex=r"QUESTION: (.*?)\n+ANSWER: ([\s\S]*)",  # или r"QUESTION: (.*?)\n+ANSWER: (.*)"
    output_keys=["query", "answer"],
    flags=re.DOTALL
)
example_gen_chain = QAGenerateChain.from_llm(llm=llm, output_parser=regex_parser)

new_examples = example_gen_chain.apply([{"doc": t} for t in data[:5]])
new_examples = [item['qa_pairs'] for item in new_examples]

#import langchain
#langchain.debug = True

#print(qa.run(new_examples[1]["qa_pairs"]["query"]))
#langchain.debug = False

predictions = qa.batch(new_examples)

eval_chain = QAEvalChain.from_llm(llm)

graded_outputs = eval_chain.evaluate(new_examples, predictions)

for i, eg in enumerate(new_examples):
    print(f"Example {i}:")
    print("Question: " + predictions[i]['query'])
    print("Real Answer: " + predictions[i]['answer'])
    print("Predicted Answer: " + predictions[i]['result'])
    print("Predicted Grade: " + graded_outputs[i]['results'])
    print()