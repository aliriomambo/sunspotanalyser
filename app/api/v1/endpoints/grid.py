"""
Router file for the Grid Endpoint
"""
import logging
from fastapi import APIRouter
from app.schemas.grid import GridCreateResponse, Grid, GridDB
from app.db.repository.grid import save_grid, get_grid, delete_grid

logger = logging.getLogger("service_logger")
router = APIRouter()


@router.post("/", response_model=GridCreateResponse)
async def create_grid(grid: Grid):
    """
    Endpoint that creates a Grid as requested by the caller
    """
    logger.info(f"Creating  the following Grid {grid.dict()}")
    created_grid = await save_grid(grid)
    logger.info(f"Grid created successfully {created_grid.dict()}")
    return created_grid.dict()


@router.get("/", response_model=GridDB)
async def get_grid_by_id(id: str):
    """
    Endpoint that gets the Grid by the ID as requested by the caller
    """
    logger.info(f"Retrieving Grid with the ID: {id}")
    retrieved_grid = await get_grid(grid_id=id)
    logger.info(f"Retrieved Grid successfully: {retrieved_grid.dict()}")
    return retrieved_grid


@router.delete("/")
async def delete_grid_endpoint(id: str):
    """
    Endpoint that deletes a Grid by the Grid ID
    :param id: ID
    :return: Status Message
    """
    logger.info(f"Deleting Grid with the ID: {id}")
    deleted_grid = await delete_grid(grid_id=id)
    logger.info(f"Deleted Grid successfully the ID: {id}")
    return deleted_grid
