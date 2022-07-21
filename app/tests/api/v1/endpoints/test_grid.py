from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_grid():
    response = client.post(
        "/api/v1/grid",
        json={
            "id": "Test",
            "size": "2",
            "values": "1,2,3,4"
        },
    )
    assert response.status_code == 200
