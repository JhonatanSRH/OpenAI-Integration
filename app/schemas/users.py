"""Users schemas"""
# Pydantic
from pydantic import BaseModel
from typing import Literal


class UserBaseSchema(BaseModel):
    """User base schema class"""
    username: str
    role: Literal['admin', 'user', 'guest']

    class Config:
        """User base schema config"""
        json_schema_extra = {
            "example": {
                "username": "jhonatanr",
                "role": "user"
            }
        }

class UserCreateSchema(UserBaseSchema):
    """User create schema class"""
    pass

class UserSchema(UserBaseSchema):
    """User schema class"""
    id: int

    class Config:
        """User schema config"""
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "jhonatanr",
                "role": "user"
            }
        }
