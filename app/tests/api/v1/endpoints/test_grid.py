"""
Test Suite for the Grid Endpoint
"""
import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio

sample_grid_values = "4, 2, 3, 2, 2, 1, 3, 2, 1"
sample_grid_size = 3


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
    Helper function to delete grids after being used at the unit tests
    :param client_test: AsyncClient created by the fixture
    :param grid_id: Grid_ID which has to be deleted
    :return: Response for the deleted grid
    """
    response = await client_test.delete(
        f"grid?id={grid_id}")
    return response


async def test_create_grid(client_test: AsyncClient) -> None:
    """Test Grid creation Endpoint"""
    response = await create_grid(client_test)
    grid_id = response.json()["id"]
    assert response.status_code == 200
    await delete_grid(client_test, grid_id)


async def test_delete_grid(client_test: AsyncClient) -> None:
    """Test Grid deletion endpoint """
    grid = await create_grid(client_test)
    grid_id = grid.json()["id"]
    response = await delete_grid(client_test, grid_id)
    assert response.status_code == 200


async def test_delete_unexistant_grid(client_test: AsyncClient):
    """Test Grid deletion with unexistant id"""
    grid = await create_grid(client_test)
    grid_id = grid.json()["id"]
    response = await delete_grid(client_test, "random_id")
    assert response.status_code == 404
    await client_test.delete(
        f"grid?id={grid_id}")


async def test_get_grid(client_test: AsyncClient) -> None:
    """Test Get Grid By ID endpoint"""
    response_grid = await create_grid(client_test)
    grid_id = response_grid.json()["id"]
    response_get_grid = await client_test.get(f"/grid?id={grid_id}")
    assert response_get_grid.status_code == 200
    await delete_grid(client_test, grid_id)


async def test_get_grid_not_found(client_test: AsyncClient) -> None:
    """Test Get Grid By ID endpoint"""
    grid_id = "random"
    response_get_grid = await client_test.get(f"/grid?id={grid_id}")
    assert response_get_grid.status_code == 404
