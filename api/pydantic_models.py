from pydantic import BaseModel, Field
from enum import Enum

class ModelName(str, Enum):
    GPT4_O = "gpt-4o"
    GPT4_O_MINI = "gpt-4o-mini"
    LLAMA3_2 = "llama3.2"

class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: ModelName = Field(default=ModelName.LLAMA3_2)

class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName
