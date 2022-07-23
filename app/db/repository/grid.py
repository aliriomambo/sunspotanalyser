"""
Grid Repository to interact with the Database
"""
from app.schemas.grid import GridDB, Grid
from beanie import PydanticObjectId
from typing import List
from app.db.repository.scores import save_scores


async def save_grid(grid: Grid) -> dict:
    """
    :param grid: Instance of grid which will be saved into the DB
    :return: created grid dictionary
    """
    grid_db = GridDB(size=grid.size, values=grid.values)
    created_grid = await grid_db.create()
    await save_scores(created_grid)
    return created_grid.dict()
