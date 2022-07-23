"""
Server app config
"""

from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.schemas.scores import ScoresSave
from app.schemas.grid import GridDB
from app.core.config import settings

app = FastAPI()


@app.on_event("startup")
async def app_init():
    """Initialize application services"""
    client = AsyncIOMotorClient(
        f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASS}@{settings.MONGO_HOST}:{settings.MONGO_PORT}"
    )

    await init_beanie(client.db, document_models=[GridDB, ScoresSave])
