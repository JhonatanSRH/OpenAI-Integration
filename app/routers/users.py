"""Users routers"""
# FastAPI
from fastapi import APIRouter, HTTPException, Depends
# Modules
from schemas.users import UserSchema, UserCreateSchema
import crud.users as crud
from config.db import get_db_session


router = APIRouter()

@router.post("/init_user/", response_model=UserSchema)
def create_user(user: UserCreateSchema, 
                session = Depends(get_db_session)) -> UserSchema:
    """Crea un usuario

    Args:
        user (UserSchema): Esquema de usuario
        session (AsyncSession, optional): sesion de base de datos. 
            Por defecto Depends(get_db_session).

    Returns:
        UserSchema: objeto esquema de usuario
    """
    return crud.insert_user(session, user)

@router.get("/users/{user_id}", response_model=UserSchema)
def retrieve_user(user_id: int, 
                  session = Depends(get_db_session)) -> UserSchema:
    """Obtiene un usuario

    Args:
        user_id (int): id de usuario a consultar
        session (AsyncSession, optional): sesion de base de datos. 
            Por defecto Depends(get_db_session).

    Returns:
        UserSchema: objeto esquema de usuario
    """
    user = crud.select_user(session, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.get("/users/", response_model=list[UserSchema])
def retrieve_user(skip: int = 0, 
                  limit: int = 10, 
                  session = Depends(get_db_session)) -> list[UserSchema]:
    """Obtiene un usuario

    Args:
        skip (int): cantidad de datos a saltar
        limit (int): limite de datos a obtener
        session (AsyncSession, optional): sesion de base de datos. 
            Por defecto Depends(get_db_session).

    Returns:
        list: lista de usuarios
    """
    users_list = crud.select_users(session, skip, limit)
    return users_list
