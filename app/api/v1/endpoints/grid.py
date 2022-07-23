"""
Router file for the Grid Endpoint
"""
from fastapi import APIRouter, HTTPException
from app.schemas.grid import GridCreateResponse, Grid, GridDB
from app.db.repository.grid import save_grid
from app.strings.errors import GRID_RECORD_NOT_FOUND, GRID_DELETED_SUCCESS

router = APIRouter()


@router.post("/", response_model=GridCreateResponse)
async def create_grid(grid: Grid):
    """
    Endpoint that creates a Grid as requested by the caller
    """
    return await save_grid(grid)


@router.delete("/")
async def delete_grid(id: str):
    """
    Endpoint that deletes a Grid by the Grid ID
    :param id: ID
    :return: Status Message
    """
    record = await GridDB.get(id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail=GRID_RECORD_NOT_FOUND
        )

    await record.delete()
    return {
        "message": GRID_DELETED_SUCCESS
    }
