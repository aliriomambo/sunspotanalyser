"""
Server app config
"""

from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from logging.config import dictConfig
from app.schemas.scores import ScoresSave
from app.schemas.grid import GridDB
from app.core.config import settings, LogConfig

dictConfig(LogConfig().dict())

app = FastAPI(debug=True)


@app.on_event("startup")
async def app_init():
    """Initialize application services"""
    uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(settings.MONGO_USER, settings.MONGO_PASS,
                                                             settings.MONGO_HOST, settings.MONGO_PORT,
                                                             settings.MONGO_DB)
    client = AsyncIOMotorClient(uri)

    await init_beanie(client.db, document_models=[GridDB, ScoresSave])
