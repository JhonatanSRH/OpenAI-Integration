"""Messages routers"""
# FastAPI
from fastapi import APIRouter, HTTPException, Depends
# Modules
from models.messages import Message
from schemas.messages import MessageBaseSchema, MessageResponseSchema
import crud.messages as crud
from config.db import get_db_session
from config import openai


router = APIRouter(prefix="/messages")

@router.post("/ask/", response_model=MessageResponseSchema)
def send_message(message_data: MessageBaseSchema,
                 session = Depends(get_db_session)) -> Message:
    """Crea un mensaje y lo envia a OpenAI

    Args:
        message (MessageBaseSchema): Esquema del mensaje para su creacion
        session (object, optional): sesion de base de datos. 
            Por defecto Depends(get_db_session).

    Returns:
        Message: objeto con datos del mensaje creado
    """
    openai_response = openai.send_message(message_data.question)
    message_res = MessageResponseSchema(user_id=message_data.user_id,
                                        question=message_data.question,
                                        response=openai_response)
    message = crud.insert_message(session, message_res)
    if message is None:
        raise HTTPException(status_code=404, detail="El mensaje no se pudo enviar")
    return message

@router.get("/history/{username}", response_model=list[MessageResponseSchema])
def filter_messages(username: str,
                    session = Depends(get_db_session)) -> list[Message]:
    """Obtiener una lista de mensajes

    Args:
        skip (int): cantidad de datos a saltar
        limit (int): limite de datos a obtener
        session (object, optional): sesion de base de datos. 
            Por defecto Depends(get_db_session).

    Returns:
        list: lista de mensajes
    """
    messages_list = crud.filter_message(session, username)
    if not messages_list:
        raise HTTPException(status_code=404, detail="Mensajes no encontrados")
    return messages_list

@router.get("/", response_model=list[MessageResponseSchema])
def list_messages(skip: int = 0,
                  limit: int = 10,
                  session = Depends(get_db_session)) -> list[Message]:
    """Obtiener una lista de mensajes

    Args:
        skip (int): cantidad de datos a saltar
        limit (int): limite de datos a obtener
        session (object, optional): sesion de base de datos. 
            Por defecto Depends(get_db_session).

    Returns:
        list: lista de mensajes
    """
    messages_list = crud.select_messages(session, skip, limit)
    return messages_list
