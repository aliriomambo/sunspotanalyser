from app.utils.scoring import generate_score, generate_score_all_grid


def test_generate_score():
    grid = [[5, 3, 1, 0], [4, 1, 1, 3, 2], [2, 3, 2, 4, 3], [0, 2, 3, 3, 2], [1, 0, 2, 4, 3]]
    score = generate_score(grid, 1, 1)
    assert score == 22


def test_generate_score_all_grid():
    grid = [[5, 3, 1, 2, 0], [4, 1, 1, 3, 2], [2, 3, 2, 4, 3], [0, 2, 3, 3, 2], [1, 0, 2, 4, 3]]
    score_list = generate_score_all_grid(grid)
    for score in score_list:
        score = score.dict()
    assert len(score_list) == len(grid) * len(grid[0])


def test_generate_score_edge():
    grid = [[5, 3, 1, 0], [4, 1, 1, 3, 2], [2, 3, 2, 4, 3], [0, 2, 3, 3, 2], [1, 0, 2, 4, 3]]
    score = generate_score(grid, 0, 0)
    assert score == 13
