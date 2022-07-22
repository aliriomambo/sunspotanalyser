from fastapi import APIRouter
from app.schemas.grid import GridCreateResponse, Grid
from app.db.repository.grid import save_grid

router = APIRouter()


@router.post("/", response_model=GridCreateResponse)
async def create_grid(grid: Grid):
    """
    Endpoint that creates a Grid as requested by the caller
    """
    return await save_grid(grid)
