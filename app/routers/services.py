"""Services routers"""
# FastAPI
from fastapi import APIRouter, Depends
# Modules
from app.config.db import get_db_session, check_db_status
from app.config.openai import check_openai_status


router = APIRouter(prefix="/services")

@router.get("/health/", responses={
    200: {
        "description": "Estado de los servicios",
        "content": {
            "application/json": {
                "example": {
                    "db_status": "OK",
                    "openai_status": "OK"
                }
            }
        }
    }
})
def health_check(session = Depends(get_db_session)) -> dict:
    """Comprueba el estado de los servicios"""
    openai_status = check_openai_status()
    db_status = check_db_status(session)
    return {
        "db_status": "OK" if db_status else "Fail", 
        "openai_status": "OK" if openai_status else "Fail"
    }
