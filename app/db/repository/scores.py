"""
Scores Repository to interact with the Database
"""
from app.schemas.grid import GridDB
from app.schemas.scores import Scores, ScoresSave
from app.utils.scoring import transform_values_into_grid, generate_score_all_grid


async def save_scores(grid: GridDB) -> ScoresSave:
    """
    :param grid: Instance of grid which will be used to generate the scores and save into the DB
    :return: scores map generated by the grid
    """
    matrix = transform_values_into_grid(grid.size, grid.values)
    scores = generate_score_all_grid(matrix)
    scores_save = ScoresSave(scores=scores.scores, grid_id=grid.id)
    return await scores_save.create()
