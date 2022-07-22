from fastapi import APIRouter
from app.api.v1.endpoints import scores, grid

api_router = APIRouter()
api_router.include_router(grid.router, tags=["Grid"], prefix='/grid')
api_router.include_router(scores.router, tags=["Scores"], prefix='/scores')
