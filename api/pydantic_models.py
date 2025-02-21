from pydantic import BaseModel, Field


class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)

class QueryResponse(BaseModel):
    answer: str
    session_id: str
