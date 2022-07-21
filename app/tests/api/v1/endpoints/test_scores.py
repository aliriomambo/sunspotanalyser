from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_scores():
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
