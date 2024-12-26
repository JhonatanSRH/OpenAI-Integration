"""Messages crud"""
# SQLAlchemy
from sqlalchemy import select
from sqlalchemy.orm import Session
# Modules
from app.models.users import User
from app.models.messages import Message
from app.schemas.messages import MessageResponseSchema


def filter_message(db: Session, username: str) -> list[Message]:
    """Obtiene un mensaje en base de datos basado en el nombre de usuario

    Args:
        db (Session): conexion a base de datos
        username (str): nombre del usuario

    Returns:
        Message: objeto mensaje encontrado
    """
    query = (
        select(Message)
        .join(User, User.id == Message.user_id)
        .where(User.username == username)
    )
    result = db.execute(query)
    return result.scalars().all()

def select_messages(db: Session, skip: int = 0, limit: int = 10) -> list[Message]:
    """Obtiene una lista de mensajes en base de datos

    Args:
        db (Session): conexion a base de datos
        skip (int): cantidad de datos a saltar
        limit (int): limite de datos a obtener

    Returns:
        list: lista de mensajes encontrados
    """
    return db.query(Message).offset(skip).limit(limit).all()

def insert_message(db: Session, message: MessageResponseSchema) -> Message | None:
    """Crea un mensaje en base de datos

    Args:
        db (Session): conexion a base de datos
        message (MessageResponseSchema): esquema del mensaje a insertar

    Returns:
        Message: objeto mensaje insertado
    """
    db_message = Message(user_id=message.user_id,
                         question=message.question,
                         response=message.response)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
