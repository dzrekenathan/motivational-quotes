from datetime import datetime
from pydantic import BaseModel
from enum import Enum



class QuoteBase(BaseModel):   
    quote: str
    author: str
    published: bool
    

class QuoteResponse(QuoteBase):
    id: int
    created_at: datetime


class QuoteCategory(str,Enum):
    motivational = "motivational"
    inspirational = "inspirational"
    success = "success"
    life = "life"
    leadership = "leadership"
    love = "love"
    happiness = "happiness"
    health = "health"
    gratitude = "gratitude"
    positivity = "positivity"
    lifelessons = "lifelessons"
    successstories = "successstories"
    relationships = "relationships"

