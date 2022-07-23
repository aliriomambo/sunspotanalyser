from beanie import init_beanie
import motor.motor_asyncio
from app.schemas.grid import GridDB
from app.schemas.scores import ScoresSave
from app.core.config import settings
from fastapi import FastAPI


def init_db(app: FastAPI):
    """
    Initialise db connection at startup
    Shutdown the db at shutdown
    :param app: FastAPI to initialise
    :return: None
    """

    @app.on_event("startup")
    async def startup_db_client():
        client = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASS}@{settings.MONGO_HOST}:{settings.MONGO_PORT}"
        )

        await init_beanie(database=client.db_name, document_models=[GridDB, ScoresSave])

    @app.on_event("shutdown")
    async def shutdown_db_client():
        app.mongodb_client.close()
