from datetime import datetime
from pydantic import BaseModel

class QuoteBase(BaseModel):   
    quote: str
    author: str
    published: bool

class QuoteResponse(QuoteBase):
    id: int
    created_at: datetime