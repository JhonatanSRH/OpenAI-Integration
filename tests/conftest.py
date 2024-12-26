"""config test"""
# Python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Pytest
import pytest
# FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlmodel import SQLModel
# Modules
from app.config.db import get_db_session
from app.main import app
from app.models.users import User
from app.models.messages import Message


DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)

@pytest.fixture(name="session")
def session_fixture():
    """Inicializa la base de datos y crea una sesión de prueba"""
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):
    """Sobrescribe la dependencia a la sesión de la base de datos por la de pruebas"""
    def override_get_session():
        yield session
    app.dependency_overrides[get_db_session] = override_get_session
    return TestClient(app)

@pytest.fixture(scope="function")
def create_initial_data(session: Session):
    """Crea datos iniciales de prueba"""
    user = User(username="jhonatan", role="admin")
    session.add(user)
    session.commit()
    session.refresh(user)
    message = Message(user_id=user.id, question="Ping?", response="Pong!")
    session.add(message)
    session.commit()
    yield
