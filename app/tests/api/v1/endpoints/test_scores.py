"""
Test Suite for the Score Endpoint
"""
from httpx import AsyncClient
import pytest

pytestmark = pytest.mark.asyncio


async def create_grid(client_test: AsyncClient):
    """
    Helper Function to create Grid for the unit tests
    :param client_test: AsyncClient created by the fixture
    :return: Response
    """
    response = await client_test.post(
        "/grid/",
        json={
            "size": "5",
            "values": "5, 3, 1, 2, 0, 4, 1, 1, 3, 2,2, 3, 2, 4, 3, 0, 2, 3, 3, 2,1, 0, 2, 4, 3"
        })
    return response


async def delete_grid(client_test: AsyncClient, grid_id: str):
    """
    :param client_test: AsyncClient created by the fixture
    :param grid_id: Grid_ID which has to be deleted
    :return: Response for the deleted grid
    """
    response = await client_test.delete(
        f"grid?id={grid_id}")
    return response


async def test_get_scores(client_test: AsyncClient) -> None:
    """Test user endpoint returns authorized user"""
    response_grid = await create_grid(client_test)
    grid_id = response_grid.json()["id"]
    response_scores = await client_test.get(f"/scores?id={grid_id}")
    assert response_scores.status_code == 200
    await delete_grid(client_test, grid_id)


async def test_get_top_scores(client_test: AsyncClient) -> None:
    """Test user endpoint returns authorized user"""
    response_grid = await create_grid(client_test)
    grid_id = response_grid.json()["id"]
    top = 2
    response_scores = await client_test.get(f"/scores?id={grid_id}&top={top}")
    assert response_scores.status_code == 200
    await delete_grid(client_test, grid_id)
