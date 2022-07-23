from fastapi import APIRouter, HTTPException
from app.schemas.grid import GridCreateResponse, Grid, GridDB
from app.db.repository.grid import save_grid

router = APIRouter()


@router.post("/", response_model=GridCreateResponse)
async def create_grid(grid: Grid):
    """
    Endpoint that creates a Grid as requested by the caller
    """
    return await save_grid(grid)


@router.delete("/")
async def delete_grid(id: str):
    record = await GridDB.get(id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Review record not found!"
        )

    await record.delete()
    return {
        "message": "Record deleted successfully"
    }
