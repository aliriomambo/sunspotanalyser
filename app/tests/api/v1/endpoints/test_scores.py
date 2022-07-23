"""
Test Suite for the Score Endpoint
"""
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_scores(client: AsyncClient) -> None:
    """Test user endpoint returns authorized user"""
    resp = await client.get("/user")
    assert resp.status_code == 200

# @pytest.mark.anyio
# async def test_get_scores():
# async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
#     response_grid = await ac.post(
#         "/grid/",
#         json={
#             "size": "5",
#             "values": "5, 3, 1, 2, 0, 4, 1, 1, 3, 2,2, 3, 2, 4, 3, 0, 2, 3, 3, 2,1, 0, 2, 4, 3"
#         }
#     )
# async with AsyncClient(app=app, base_url="http://test") as ac:
#     response = await ac.get(f"/scores?id=a6d86406-c88c-4b82-8005-3316bc641577")
#
# # response = await client_test.get("/scores?id=3a1b1412-ee3a-4548-ba9d-06579529cc36")
# assert response.status_code == 200
# # assert response.json() == {"message": "Hello World"}
