"""
Grid Schema file where all the Schemas related to Grid are centralized
"""
from pydantic import BaseModel, root_validator
from uuid import uuid4
from beanie import Document
from app.strings.errors import NON_INTEGER_VALUE, VALUE_OUT_OF_RANGE, MISMATCH_SIZE_VALUES


class Grid(BaseModel):
    """
    Schema related to Grid which is used on the endpoint
    """
    size: int
    values: str

    @root_validator
    def validate_all(cls, grid):
        values = [x.strip() for x in grid['values'].split(',')]
        all_values_digits = [v for v in values if v.isdigit()]

        if not all_values_digits:
            raise ValueError(NON_INTEGER_VALUE)

        sorted_values = [int(number) for number in values]
        sorted_values.sort()
        if sorted_values[0] < 0 or sorted_values[-1] > 5:
            raise ValueError(VALUE_OUT_OF_RANGE)

        if int(grid['size'] ** 2) != len(sorted_values):
            raise ValueError(MISMATCH_SIZE_VALUES)
        return grid

    class Config(object):
        """
            Sample Schema template for the OpenApi specification
        """
        schema_extra = {
            "example": {
                "size": "2",
                "values": "1,2,3,4"
            }
        }


class GridDB(Document):
    """
    Schema related to Grid which is used to save the grid on the database
    """
    id: str = str(uuid4())
    size: int
    values: str

    class Settings(object):
        "Collection Name for the database"
        name = "grid_collection"


class GridCreateResponse(BaseModel):
    """
    Schema used as the Response Model for the post endpoint
    """
    id: str
