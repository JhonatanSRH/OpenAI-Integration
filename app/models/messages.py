"""Messages models"""
# SQLModel
from typing import Optional
from sqlmodel import SQLModel, Field


class Message(SQLModel, table=True):
    """Message model class"""
    __tablename__ = 'messages'

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key='users.id')
    question: str
    response: str
