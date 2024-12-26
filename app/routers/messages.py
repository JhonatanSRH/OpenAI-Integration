"""Messages routers"""
# FastAPI
from fastapi import APIRouter, HTTPException, Depends
# Modules
from app.models.messages import Message
from app.schemas.messages import MessageBaseSchema, MessageResponseSchema
import app.crud.messages as crud
from app.config.db import get_db_session
from app.config import openai


router = APIRouter(prefix="/messages")

@router.post("/ask/", 
             response_model=MessageResponseSchema, 
             responses={400: {"description": "El mensaje no se pudo enviar"}})
def send_message(message_data: MessageBaseSchema,
                 session = Depends(get_db_session)) -> Message:
    """Crea un mensaje y lo envia a OpenAI"""
    openai_response = openai.send_message(message_data.question)
    message_res = MessageResponseSchema(user_id=message_data.user_id,
                                        question=message_data.question,
                                        response=openai_response)
    message = crud.insert_message(session, message_res)
    if message is None:
        raise HTTPException(status_code=400, detail="El mensaje no se pudo enviar")
    return message

@router.get("/history/{username}/", 
            response_model=list[MessageResponseSchema],
            responses={404: {"description": "Mensajes no encontrados"}})
def filter_messages(username: str,
                    session = Depends(get_db_session)) -> list[Message]:
    """Obtiener una lista de mensajes"""
    messages_list = crud.filter_message(session, username)
    if not messages_list:
        raise HTTPException(status_code=404, detail="Mensajes no encontrados")
    return messages_list

@router.get("/", response_model=list[MessageResponseSchema])
def list_messages(skip: int = 0,
                  limit: int = 10,
                  session = Depends(get_db_session)) -> list[Message]:
    """Obtiener una lista de mensajes"""
    messages_list = crud.select_messages(session, skip, limit)
    return messages_list
