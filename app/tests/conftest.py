import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from app.main import app
from typing import Iterator


@pytest.fixture()
async def client() -> Iterator[AsyncClient]:
    """
    Create an instance of the client.
    :return: yield HTTP client.
    """
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as _client:
            try:
                yield _client
            except Exception as exc:
                print(exc)
