"""
    Scoring utils which is used to generate Scores based on the Grid
"""
from app.schemas.scores import Score, Scores
from typing import List


def transform_values_into_grid(size: int, values: str) -> List:
    """
    Function that transform Grid Values into a Matrix of scores
    :param size: matrix size
    :param values: values of the matrix
    :return: List (matrix)
    """
    matrix = []
    values = [int(x.strip()) for x in values.split(',')]
    counter = 0
    for _ in range(0, size):
        row_list = []
        for _ in range(0, size):
            row_list.append(values[counter])
            counter = counter + 1
        matrix.append(row_list)
    return matrix


def sort_by_n_top_scores(scores, top) -> Scores:
    """
    Function that sorts the scores descendingly and retrieves the top n scores
    :param scores: List of Scores
    :param top: Number of top scores to retrieve
    :return: Scores
    """
    scores = Scores(scores=scores.scores).dict()
    scores_values_list = sort_score_grid(scores['scores'])
    scores_values_list = scores_values_list[:top]
    new_scores: Scores = Scores(scores=scores_values_list)
    return new_scores


def sort_score_grid(score_grid: List[dict]) -> List[dict]:
    """
    Sort the score matrix by the score
    :param score_grid: score matrix
    :return: List[dict]
    """
    return sorted(score_grid, key=lambda d: d['score'], reverse=True)


def generate_score_all_grid(grid) -> Scores:
    """
    Generate the score for the entire grid
    :param grid: Grid
    :return: Scores which contain score for each cell of the grid
    """
    score_list = []

    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            current_score = generate_score(grid, x, y)
            score = Score(x=x, y=y, score=current_score)
            score_list.append(score)
    scores = Scores(scores=score_list)
    return scores


def generate_score(grid, x, y) -> int:
    """

    :param grid: Matrix of heat values
    :param x: row position of matrix
    :param y: column position of matrix
    :return: int which represents the current location score
    """
    heat_values_list = __get_grid_heat_values(grid, x, y)
    score = sum(heat_values_list)
    return score


def __get_grid_heat_values(grid, x, y) -> List:
    """
    Function that calculates the score at the specified position
    :param grid: Matrix of heat values
    :param x: row position of matrix
    :param y: column position of matrix
    :return: List of surrounding heat values including the actual position
    """
    heat_value_list = sum((row[x - (x > 0): x + 2]
                           for row in grid[y - (y > 0):y + 2]), [])
    return heat_value_list
