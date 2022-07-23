"""
Router file for the Scores Endpoint
"""
from fastapi import APIRouter
from app.schemas.scores import ScoresSave, Scores

router = APIRouter()


@router.get("/", response_model=Scores)
async def get_scores(id: str):
    """
    Endpoint that gets the score by the GRID_ID as requested by the caller
    """
    scores = await ScoresSave.find_one(ScoresSave.grid_id == id)
    return scores
