"""
Router file for the Scores Endpoint
"""
from fastapi import APIRouter, HTTPException
from app.schemas.scores import Scores, Score
from app.db.repository.scores import get_scores_by_id, get_scores_by_location
from app.strings.errors import TOP_VALUE_INVALID

router = APIRouter()


@router.get("/", response_model=Scores)
async def get_scores(id: str, top: int = None):
    """
    Endpoint that gets the score by the GRID_ID as requested by the caller
    """
    if top and top <= 0:
        raise HTTPException(
            status_code=400,
            detail=TOP_VALUE_INVALID
        )
    return await get_scores_by_id(id, top)


@router.get("/location/", response_model=Score)
async def get_scores_by_loc(id: str, x: int, y: int):
    """
    Endpoint that gets the score by the location
    """
    return await get_scores_by_location(id, x, y)
