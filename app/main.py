from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.api import api_router
from app.db.database import init_db

app = FastAPI(
    title='Sun Spot Analyser', openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def start_db():
    await init_db()
