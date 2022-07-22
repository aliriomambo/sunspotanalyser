from app.schemas.grid import GridDB


async def save_scores(grid: GridDB) -> dict:
    grid_db = GridDB(size=grid.size, values=grid.values)
    created_grid = await grid_db.create()
    return created_grid.dict()
