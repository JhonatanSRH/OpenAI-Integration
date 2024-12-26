"""Users test"""
# FastAPI
from fastapi.testclient import TestClient


def test_get_users(client: TestClient):
    """Prueba obtener lista de usuarios"""
    client.post("/users/init_user/", 
                json={"username": "luis", "role": "user"})
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[-1]["username"] == "luis"

def test_create_user(client: TestClient):
    """Prueba crear usuario"""
    body = {
        "username": "jhonatanr", 
        "role": "admin"
    }
    response = client.post("/users/init_user/", json=body)
    assert response.status_code == 200
    data = response.json()
    assert data.get('message') == "Usuario creado correctamente"

def test_error_create_user(client: TestClient):
    """Prueba error de crear usuario"""
    body = {
        "username": "jhonatanr"
    }
    response = client.post("/users/init_user/", json=body)
    assert response.status_code == 422
    data = response.json()
    assert data.get('detail', [])[0].get('msg')== "Field required"
