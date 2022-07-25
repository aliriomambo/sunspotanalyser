"""
Grid Repository to interact with the Database
"""
from app.schemas.grid import GridDB, Grid
from fastapi import HTTPException
from app.db.repository.scores import save_scores, delete_scores
from app.strings.errors import GRID_DELETED_SUCCESS, GRID_RECORD_NOT_FOUND
import uuid


async def save_grid(grid: Grid) -> GridDB:
    """
    :param grid: Instance of grid which will be saved into the DB
    :return: created grid dictionary
    """
    _id = uuid.uuid4()
    _id = str(_id)
    grid_db = GridDB(id=_id, size=grid.size, values=grid.values)
    created_grid = await grid_db.create()
    await save_scores(created_grid)

    return created_grid


async def get_grid(grid_id: str) -> GridDB:
    """
    Function which retrieves the Grid from the Database using the ID
    :param grid_id: Grid ID
    :return: Grid database Record
    """
    grid = await GridDB.get(grid_id)

    if not grid:
        raise HTTPException(
            status_code=404,
            detail=GRID_RECORD_NOT_FOUND
        )
    return grid


async def delete_grid(grid_id: str) -> dict:
    """
     Endpoint that deletes a Grid by the Grid ID
     :param id: Grid ID
     :return: Status Message
    """
    record = await get_grid(grid_id=grid_id)
    if not record:
        raise HTTPException(
            status_code=404,
            detail=GRID_RECORD_NOT_FOUND
        )

    await record.delete()
    await delete_scores(grid_id)
    return {
        "message": GRID_DELETED_SUCCESS
    }
