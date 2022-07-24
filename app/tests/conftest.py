"""
Conftest Module to configure the Injected AsyncClient
"""
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from app.main import app
import pytest_asyncio


@pytest_asyncio.fixture
async def client_test():
    """
    Create an instance of the client.
    :return: yield HTTP client.
    """
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test/sun-spot-analyser-api", follow_redirects=True) as ac:
            try:
                yield ac
            except Exception as exc:
                print(exc)
