from beanie import init_beanie
import motor.motor_asyncio
from app.schemas.grid import GridDB
from app.core.config import settings


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://admin:admin@localhost:27017"
    )

    await init_beanie(database=client.db_name, document_models=[GridDB])
