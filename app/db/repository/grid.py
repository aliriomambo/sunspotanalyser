from app.schemas.grid import GridDB, Grid
from beanie import PydanticObjectId
from typing import List
from app.db.repository.scores import save_scores


async def save_grid(grid: Grid) -> dict:
    grid_db = GridDB(size=grid.size, values=grid.values)
    created_grid = await grid_db.create()
    await save_scores(created_grid)
    return created_grid.dict()


async def get_grid(id: PydanticObjectId) -> GridDB:
    grid_db = await GridDB.get(id)
    return grid_db


async def get_grids() -> List[GridDB]:
    grids = await GridDB.find_all().to_list()
    return grids
