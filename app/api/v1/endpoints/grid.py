from fastapi import APIRouter, Depends
from app.schemas.grid import GridDB

router = APIRouter()


@router.post("/grid")
async def create_grid(grid: GridDB) -> dict:
    await grid.create()
    return {"message": "Grid Created"}
