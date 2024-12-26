"""Messages schemas"""
# Pydantic
from pydantic import BaseModel, ConfigDict


class MessageBaseSchema(BaseModel):
    """Message base schema class"""
    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "user_id": 1,
                "question": "pregunta aleatoria"
            }
        })

    user_id: int
    question: str

class MessageResponseSchema(MessageBaseSchema):
    """Message response schema class"""
    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "user_id": 1,
                "question": "pregunta aleatoria",
                "response": "respuesta aleatoria"
            }
        })
    user_id: int
    question: str
    response: str
