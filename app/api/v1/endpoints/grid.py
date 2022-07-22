from fastapi import APIRouter
from app.schemas.grid import GridDB, GridCreateResponse, Grid
from app.db.repository.grid import save_grid

router = APIRouter()


@router.post("/", response_model=GridCreateResponse)
async def create_grid(grid: Grid):
    return await save_grid(grid)
