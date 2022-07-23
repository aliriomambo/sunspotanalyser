"""
Router file for the Scores Endpoint
"""
from fastapi import APIRouter, HTTPException
from app.schemas.scores import Scores
from app.db.repository.scores import get_scores_by_id

router = APIRouter()


@router.get("/", response_model=Scores)
async def get_scores(id: str, top: int = None):
    """
    Endpoint that gets the score by the GRID_ID as requested by the caller
    """
    if top and top <= 0:
        raise HTTPException(
            status_code=400,
            detail="Top value is Invalid"
        )
    return await get_scores_by_id(id, top)
