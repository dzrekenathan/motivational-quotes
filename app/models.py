from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text
from .database import Base


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, nullable=False)
    quote = Column(String, nullable=False)
    author = Column(String, nullable=True)
    published = Column(Boolean, nullable=False, server_default="True")
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)