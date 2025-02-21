from pydantic_models import QueryInput, QueryResponse
from fastapi import FastAPI
import uuid
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

app = FastAPI()

@app.post("/chat", response_model=QueryResponse)
def chat(query_input: QueryInput):
    session_id = query_input.session_id or str(uuid.uuid4())
    logging.info(f"Session ID: {session_id}, User Query: {query_input.question}")
    answer = "Accepted"
    logging.info(f"Session ID: {session_id}, AI Response: {answer}")
    return QueryResponse(answer=answer, session_id=session_id)