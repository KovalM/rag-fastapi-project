from langchain_community.chat_models.ollama import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory, ConversationTokenBufferMemory

llm = ChatOllama(temperature=0.0, model="llama3.2")

memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True
)

conversation.predict(input="Hi, my name is Andrew")
conversation.predict(input="What is 1+1?")
conversation.predict(input="What is my name?")
print(memory.buffer)
memory.load_memory_variables({})
