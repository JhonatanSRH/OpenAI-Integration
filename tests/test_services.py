"""Messages test"""
# FastAPI
from fastapi.testclient import TestClient
from unittest.mock import patch


def test_health_check(client: TestClient):
    """Prueba de estado de salud"""
    response = client.get("/services/health/")
    assert response.status_code == 200
    assert response.json().get("db_status") and response.json().get("openai_status")

def test_bad_health_check(client: TestClient):
    """Prueba de mal estado de salud"""
    with patch('app.routers.services.check_openai_status', return_value=False):
        response = client.get("/services/health/")
        assert response.status_code == 200
        assert response.json().get("openai_status") == "Fail"
