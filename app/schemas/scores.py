"""
Score Schema file where all the Schemas related to Score are centralized
"""
from pydantic import BaseModel, conint
from typing import List
from beanie import Document


class Score(BaseModel):
    """
    Schema related to Score which is used as a unit of Scores
    """
    x: conint(ge=0)
    y: conint(ge=0)
    score: conint(ge=0)


class Scores(BaseModel):
    """
    Schema that stores all of the Grid Scores into a single Schema
    """
    scores: List[Score]


class ScoresSave(Document):
    """
    Schema that is used to save the grid scores into the database
    """
    grid_id: str
    scores: List[Score]
