"""
Main Routing Configuration File
"""
from fastapi import APIRouter
from app.api.v1.endpoints import scores, grid
from app.core.config import settings

api_router = APIRouter(prefix='/sun-spot-analyser-api')
api_router.include_router(grid.router, tags=["Grid"], prefix=settings.GRID_ROUTER_PREFIX)
api_router.include_router(scores.router, tags=["Scores"], prefix=settings.SCORES_ROUTER_PREFIX)
