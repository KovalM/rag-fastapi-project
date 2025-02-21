from pydantic_models import QueryInput, QueryResponse
from langchain_utils import get_rag_chain
from fastapi import FastAPI
import uuid
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

app = FastAPI()

@app.post("/chat", response_model=QueryResponse)
def chat(query_input: QueryInput):
    session_id = query_input.session_id or str(uuid.uuid4())
    logging.info(f"Session ID: {session_id}, User Query: {query_input.question}, , Model: {query_input.model.value}")
    
    rag_chain = get_rag_chain(query_input.model.value)
    answer = rag_chain.invoke({
        "input": query_input.question,
        "context": ""
    })

    logging.info(f"Session ID: {session_id}, AI Response: {answer}")
    return QueryResponse(answer=answer, session_id=session_id, model=query_input.model)