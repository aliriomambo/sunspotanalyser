from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/")
async def get_scores():
    return {"message": "Hello World"}
