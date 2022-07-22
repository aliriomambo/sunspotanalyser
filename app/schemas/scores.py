from pydantic import BaseModel, conint
from typing import List
from beanie import Document


class Score(BaseModel):
    x: conint(ge=0)
    y: conint(ge=0)
    score: conint(ge=0)

    class Config:
        orm_mode = True


class ScoreCreate(Score):
    grid_id: int


class Scores(BaseModel):
    scores: List[Score]


class ScoresSave(Document):
    grid_id: str
    scores: List[Score]
