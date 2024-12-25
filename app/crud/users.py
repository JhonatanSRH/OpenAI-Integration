"""Users crud"""
# SQLAlchemy
from sqlalchemy.orm import Session
# Modules
from models.users import User
from schemas.users import UserCreateSchema


def select_user(db: Session, user_id: int) -> User:
    """Obtiene un usuario en base de datos

    Args:
        db (Session): conexion a base de datos
        user_id (int): id de usuario

    Returns:
        User: objeto de usuario encontrado
    """
    return db.query(User).filter(User.id == user_id).first()

def select_users(db: Session, skip: int = 0, limit: int = 10)  -> list[User]:
    """Obtiene una lista de usuarios en base de datos

    Args:
        db (Session): conexion a base de datos
        skip (int): cantidad de datos a saltar
        limit (int): limite de datos a obtener

    Returns:
        list: lista de usuarios encontrados
    """
    return db.query(User).offset(skip).limit(limit).all()

def insert_user(db: Session, user: UserCreateSchema) -> User:
    """Crea un usuario en base de datos

    Args:
        db (Session): conexion a base de datos
        user (UserCreateSchema): esquema del usuario a insertar

    Returns:
        User: objeto de usuario insertado
    """
    db_user = User(username=user.username, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
