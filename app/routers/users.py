"""Users routers"""
# FastAPI
from fastapi import APIRouter, HTTPException, Depends
# Modules
from models.users import User
from schemas.users import UserSchema, UserBaseSchema
import crud.users as crud
from config.db import get_db_session


router = APIRouter(prefix="/users")

@router.post("/init_user/")
def create_user(user_data: UserBaseSchema,
                session = Depends(get_db_session)) -> dict:
    """Crea un usuario

    Args:
        user (UserBaseSchema): Esquema de usuario para su creacion
        session (object, optional): sesion de base de datos. 
            Por defecto Depends(get_db_session).

    Returns:
        UserSchema: objeto esquema de usuario
    """
    user = crud.insert_user(session, user_data)
    if user is None:
        raise HTTPException(status_code=404, detail="El usuario no se pudo insertar")
    return {"message": "Usuario creado correctamente"}

@router.get("/{user_id}", response_model=UserSchema)
def retrieve_user(user_id: int,
                  session = Depends(get_db_session)) -> User | None:
    """Obtiene un usuario

    Args:
        user_id (int): id de usuario a consultar
        session (object, optional): sesion de base de datos. 
            Por defecto Depends(get_db_session).

    Returns:
        UserSchema: objeto esquema de usuario
    """
    user = crud.select_user(session, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.get("/", response_model=list[UserSchema])
def list_user(skip: int = 0,
              limit: int = 10,
              session = Depends(get_db_session)) -> list[User]:
    """Obtiener una lista de usuarios

    Args:
        skip (int): cantidad de datos a saltar
        limit (int): limite de datos a obtener
        session (object, optional): sesion de base de datos. 
            Por defecto Depends(get_db_session).

    Returns:
        list: lista de usuarios
    """
    users_list = crud.select_users(session, skip, limit)
    return users_list
