"""Messages test"""
# FastAPI
from fastapi.testclient import TestClient
from tests.conftest import create_initial_data


def test_filter_messages(create_initial_data, client: TestClient):
    """Prueba filtrar mensajes"""
    response = client.get("/messages/history/jhonatan/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0].get('question') == "Ping?"
    assert data[0].get('response') == "Pong!"

def test_error_filter_messages(client: TestClient):
    """Prueba error de filtrar mensajes"""
    response = client.get("/messages/history/jhonatan/")
    assert response.status_code == 404
    data = response.json()
    assert data.get('detail') == "Mensajes no encontrados"

def test_create_messages(client: TestClient):
    """Prueba crear mensajes"""
    response = client.post("/messages/ask/", 
                           json={"question": "¿Qué es un hiato?", "user_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert data.get('question') == "¿Qué es un hiato?"
    assert data.get('user_id') == 1

def test_error_create_messages(client: TestClient):
    """Prueba error de crear mensajes"""
    response = client.post("/messages/ask/", 
                           json={"user_id": 1})
    assert response.status_code == 422
    data = response.json()
    assert data.get('detail', [])[0].get('msg') == "Field required"
