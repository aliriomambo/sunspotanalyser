"""
Router file for the Scores Endpoint
"""
import logging
from fastapi import APIRouter
from app.schemas.scores import Scores, Score
from app.db.repository.scores import get_scores_by_id, get_scores_by_location

router = APIRouter()

logger = logging.getLogger("service_logger")


@router.get("/", response_model=Scores)
async def get_scores(id: str, top: int = None):
    """
    Endpoint that gets the score by the GRID_ID as requested by the caller
    """
    logger.info(f"Retrieving the Matrix score for with Grid with ID {id}")
    retrieved_scores = await get_scores_by_id(id, top)
    logger.info(f"Retrieved Scores Successfully {retrieved_scores}")
    return retrieved_scores


@router.get("/location/", response_model=Score)
async def get_scores_by_loc(id: str, x: int, y: int):
    """
    Endpoint that gets the score by the location
    """
    logger.info(f"Retrieving the Matrix score for with Grid with ID {id} and X: {x} and Y: {y}")
    retrieved_scores = await get_scores_by_location(id, x, y)
    logger.info(f"Retrieved Scores Successfully {retrieved_scores}")
    return retrieved_scores
