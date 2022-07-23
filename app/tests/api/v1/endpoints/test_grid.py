"""
Test Suite for the Grid Endpoint
"""
from httpx import AsyncClient
import pytest

pytestmark = pytest.mark.asyncio

sample_grid_values = "4, 2, 3, 2, 2, 1, 3, 2, 1"
sample_grid_size = 3


async def create_grid(client_test: AsyncClient):
    response = await client_test.post(
        "/grid/",
        json={
            "size": "5",
            "values": "5, 3, 1, 2, 0, 4, 1, 1, 3, 2,2, 3, 2, 4, 3, 0, 2, 3, 3, 2,1, 0, 2, 4, 3"
        })
    return response


async def delete_grid(client_test: AsyncClient, grid_id: str):
    response = await client_test.delete(
        f"grid?id={grid_id}")
    return response


async def test_create_grid(client_test: AsyncClient) -> None:
    """Test user endpoint returns authorized user"""
    response = await create_grid(client_test)
    grid_id = response.json()["id"]
    assert response.status_code == 200
    await delete_grid(client_test, grid_id)


async def test_delete_grid(client_test: AsyncClient) -> None:
    """Test user endpoint returns authorized user"""
    grid = await create_grid(client_test)
    grid_id = grid.json()["id"]
    response = await delete_grid(client_test, grid_id)
    assert response.status_code == 200
