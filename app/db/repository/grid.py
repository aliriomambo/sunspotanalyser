from app.schemas.grid import GridDB, Grid


async def save_grid(grid: Grid) -> dict:
    grid_db = GridDB(size=grid.size, values=grid.values)
    created_grid = await grid_db.create()
    return created_grid.dict()
