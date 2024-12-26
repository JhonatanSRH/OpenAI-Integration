"""Messages schemas"""
# Pydantic
from pydantic import BaseModel


class MessageBaseSchema(BaseModel):
    """Message base schema class"""
    user_id: int
    question: str

    class Config:
        """Message base schema config"""
        json_schema_extra = {
            "example": {
                "user_id": 1,
                "question": "pregunta aleatoria"
            }
        }

class MessageResponseSchema(MessageBaseSchema):
    """Message response schema class"""
    user_id: int
    question: str
    response: str

    class Config:
        """Message response schema config"""
        json_schema_extra = {
            "example": {
                "user_id": 1,
                "question": "pregunta aleatoria",
                "response": "respuesta aleatoria"
            }
        }
