"""main module"""
# FastAPI
from fastapi import FastAPI
# Routers
from app.routers.messages import router as messages_router
from app.routers.services import router as services_router
from app.routers.users import router as user_router


app = FastAPI(title="API Chatbot", version="0.1.0")

# Routers
app.include_router(messages_router)
app.include_router(services_router)
app.include_router(user_router)
