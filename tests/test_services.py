"""Messages test"""
# FastAPI
from fastapi.testclient import TestClient


def test_health_check(client: TestClient):
    """Prueba de estado de salud"""
    response = client.get("/services/health/")
    assert response.status_code == 200
    assert response.json().get("db_status") and response.json().get("openai_status")

def test_bad_health_check(client: TestClient, monkeypatch):
    """Prueba de mal estado de salud"""
    monkeypatch.setenv("OPENAI_API_KEY", "invalid_api_key")
    response = client.get("/services/health/")
    assert response.status_code == 200
    assert response.json().get("openai_status") == "Fail"
