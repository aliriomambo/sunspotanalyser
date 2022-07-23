"""
Test Suite for the Grid Endpoint
"""
from httpx import AsyncClient
from app.main import app
from fastapi.testclient import TestClient

client_test = TestClient(app)

pytest_plugins = ('pytest_asyncio',)


async def test_create_grid() -> None:
    """Test user endpoint returns authorized user"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/grid/",
            json={
                "size": "5",
                "values": "5, 3, 1, 2, 0, 4, 1, 1, 3, 2,2, 3, 2, 4, 3, 0, 2, 3, 3, 2,1, 0, 2, 4, 3"
            })
    assert response.status_code == 200
