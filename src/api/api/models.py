from pydantic import BaseModel, Field
from typing import Optional, List

class RAGRequest(BaseModel):
    query: str = Field(..., description="The query to used in the RAG pipepine")

class RAGUsedContext(BaseModel):
    image_url: str = Field(..., description="The image URL of the item")
    price: Optional[float] = Field(..., description="The price of the item")
    description: str = Field(..., description="The description of the item")

class RAGResponse(BaseModel):
    # to be implemented in the middleware
    request_id: str = Field(..., description="The request ID")
    answer: str = Field(..., description="The answer to the query")
    used_context: List[RAGUsedContext] = Field(..., description="Information about items used to answer the query")