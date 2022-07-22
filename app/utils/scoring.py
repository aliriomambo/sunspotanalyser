def generate_score(grid, x, y):
    heat_values_list = __get_grid_heat_values(grid, x, y)
    score = sum(heat_values_list)
    return score


def __get_grid_heat_values(grid, x, y):
    heat_value_list = sum((row[y - (y > 0): y + 2]
                           for row in grid[x - (x > 0):x + 2]), [])
    return heat_value_list
