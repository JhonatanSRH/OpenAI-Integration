"""main module"""
# FastAPI
from fastapi import FastAPI
# Routers
from routers.messages import router as messages_router
from routers.services import router as services_router
from routers.users import router as user_router


app = FastAPI()

# Routers
app.include_router(messages_router)
app.include_router(services_router)
app.include_router(user_router)
