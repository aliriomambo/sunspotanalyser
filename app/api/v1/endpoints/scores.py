from fastapi import APIRouter, Depends
from app.schemas.scores import Scores, ScoresSave, ScoresGet
from app.schemas.grid import GridDB
from beanie import PydanticObjectId
from app.utils.scoring import generate_score_all_grid, transform_values_into_grid
from app.db.repository.scores import retrieve_scores

router = APIRouter()


@router.get("/{id}", response_model=ScoresGet)
async def get_scores(id: str):
    scores = await ScoresSave.find_one(ScoresSave.grid_id == id)
    return scores
