from pydantic import BaseModel, Field


class RAGRequest(BaseModel):
    query: str = Field(..., description="The query to used in the RAG pipepine")


class RAGResponse(BaseModel):
    # to be implemented in the middleware
    request_id: str = Field(..., description="The request ID")
    answer: str = Field(..., description="The answer to the query")