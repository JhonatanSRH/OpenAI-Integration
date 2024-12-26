"""Users models"""
# SQLModel
from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    """User model class"""
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    role: str
