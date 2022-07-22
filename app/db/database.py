from beanie import init_beanie
import motor.motor_asyncio
from app.schemas.grid import GridDB
from app.schemas.scores import ScoresSave
from app.core.config import settings


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASS}@{settings.MONGO_HOST}:{settings.MONGO_PORT}"
    )

    await init_beanie(database=client.db_name, document_models=[GridDB, ScoresSave])
