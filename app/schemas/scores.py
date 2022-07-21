from pydantic import BaseModel, conint
from typing import List


class Score(BaseModel):
    x: conint(ge=0)
    y: conint(ge=0)
    score: conint(ge=0)

    class Config:
        orm_mode = True


class ScoreCreate(Score):
    grid_id: int


class Scores(BaseModel):
    __root__: List[Score]

    class Config:
        orm_mode = True
