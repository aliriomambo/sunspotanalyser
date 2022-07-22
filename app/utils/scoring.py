from app.schemas.scores import Score
from typing import List


def sort_score_grid(score_grid: List[dict]) -> List[dict]:
    return sorted(score_grid, key=lambda d: d['score'], reverse=True)


def generate_score_all_grid(grid) -> List[Score]:
    score_list = []

    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            current_score = generate_score(grid, x, y)
            score = Score(x=x, y=y, score=current_score)
            score_list.append(score)

    return score_list


def generate_score(grid, x, y):
    heat_values_list = __get_grid_heat_values(grid, x, y)
    score = sum(heat_values_list)
    return score


def __get_grid_heat_values(grid, x, y):
    heat_value_list = sum((row[y - (y > 0): y + 2]
                           for row in grid[x - (x > 0):x + 2]), [])
    return heat_value_list
