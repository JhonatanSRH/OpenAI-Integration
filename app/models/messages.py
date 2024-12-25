"""Messages models"""
# FastAPI
from sqlmodel import SQLModel, Field 
from typing import Optional


class Message(SQLModel, table=True):
    """Message model class"""
    __tablename__ = 'messages'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key='user_id')
    question: str 
    response: str 
