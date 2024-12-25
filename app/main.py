"""main module"""
# FastAPI
from fastapi import FastAPI
# Routers
from routers.users import router as user_router


app = FastAPI()

app.include_router(user_router)
