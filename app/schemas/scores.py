from pydantic import BaseModel, conint
from typing import List


class Score(BaseModel):
    x: conint(ge=0)
    y: conint(ge=0)
    score: conint(ge=0)


class Scores(BaseModel):
    __root__: List[Score]

