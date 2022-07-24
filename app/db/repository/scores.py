"""
Scores Repository to interact with the Database
"""
from app.schemas.grid import GridDB
from app.schemas.scores import ScoresSave, Score, Scores
from app.utils.scoring import transform_values_into_grid, generate_score_all_grid, sort_by_n_top_scores
from fastapi import HTTPException
from app.strings.errors import SCORES_GRID_DOESNT_EXIST, GRID_RECORD_NOT_FOUND
from app.strings.errors import SCORES_GRID_DOESNT_EXIST


async def get_scores_by_id(id: str, top: int = None):
    """
    Function that returns the scores and with the option of top n scores
    :param id: Grid ID
    :param top: Top N scores
    :return: Scores
    """
    grid = await GridDB.get(id)

    if not grid:
        raise HTTPException(
            status_code=404,
            detail=GRID_RECORD_NOT_FOUND
        )
    scores = await ScoresSave.find_one(ScoresSave.grid_id == id)

    if not top:
        return scores
    else:
        return sort_by_n_top_scores(scores, top)


async def get_scores_by_location(id: str, x: int, y: int) -> Score:
    """
    Function that returns the score by the specific grid location
    :param id: Grid ID
    :param x: Row Location
    :param y: Column Location
    :return: Score
    """
    scores = await ScoresSave.find_one(ScoresSave.grid_id == id)
    if not scores:
        raise HTTPException(
            status_code=404,
            detail=GRID_RECORD_NOT_FOUND)

    scores = Scores(scores=scores.scores).dict()
    for score in scores['scores']:
        if score['x'] == x and score['y'] == y:
            return Score(x=x, y=y, score=score['score'])

    raise HTTPException(
        status_code=404,
        detail="Location Not Found"
    )


async def save_scores(grid: GridDB) -> ScoresSave:
    """
    :param grid: Instance of grid which will be used to generate the scores and save into the DB
    :return: scores map generated by the grid
    """
    matrix = transform_values_into_grid(grid.size, grid.values)
    scores = generate_score_all_grid(matrix)
    scores_save = ScoresSave(scores=scores.scores, grid_id=grid.id)
    return await scores_save.create()


async def delete_scores(grid_id: str):
    """
    Function to delete scores when the grid is deleted
    :param grid_id: Grid ID
    :return: None
    """
    scores = await ScoresSave.find_one(ScoresSave.grid_id == grid_id)
    if scores:
        await scores.delete()
