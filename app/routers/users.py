"""Users routers"""
# FastAPI
from fastapi import APIRouter, HTTPException, Depends
# Modules
from app.models.users import User
from app.schemas.users import UserSchema, UserBaseSchema
import app.crud.users as crud
from app.config.db import get_db_session


router = APIRouter(prefix="/users")

@router.post("/init_user/", responses={
    400: {"description": "El usuario no se pudo insertar"},
    200: {"description": "Usuario creado correctamente"}
})
def create_user(user_data: UserBaseSchema,
                session = Depends(get_db_session)) -> dict:
    """Crea un usuario"""
    user = crud.insert_user(session, user_data)
    if user is None:
        raise HTTPException(status_code=400, detail="El usuario no se pudo insertar")
    return {"message": "Usuario creado correctamente"}

@router.get("/{user_id}/", 
            response_model=UserSchema,
            responses={404: {"description": "Usuario no encontrado"}})
def retrieve_user(user_id: int,
                  session = Depends(get_db_session)) -> User | None:
    """Obtiene un usuario"""
    user = crud.select_user(session, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.get("/", response_model=list[UserSchema])
def list_user(skip: int = 0,
              limit: int = 10,
              session = Depends(get_db_session)) -> list[User]:
    """Obtiener una lista de usuarios"""
    users_list = crud.select_users(session, skip, limit)
    return users_list
