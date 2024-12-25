"""Users models"""
# FastAPI
from sqlmodel import SQLModel, Field 
from typing import Optional


class User(SQLModel, table=True):
    """User model class"""
    __tablename__ = 'users'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    role: str