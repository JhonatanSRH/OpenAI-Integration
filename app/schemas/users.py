"""Users schemas"""
# Pydantic
from typing import Literal
from pydantic import BaseModel, ConfigDict


class UserBaseSchema(BaseModel):
    """User base schema class"""
    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "username": "jhonatanr",
                "role": "user"
            }
        })

    username: str
    role: Literal['admin', 'user', 'guest']

class UserSchema(UserBaseSchema):
    """User schema class"""
    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "jhonatanr",
                "role": "user"
            }
        })

    id: int
