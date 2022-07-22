from app.utils.scoring import generate_score


def test_generate_score():
    grid = [[5, 3, 1, 0], [4, 1, 1, 3, 2], [2, 3, 2, 4, 3], [0, 2, 3, 3, 2], [1, 0, 2, 4, 3]]
    score = generate_score(grid, 1, 1)
    assert score == 22


def test_generate_score_edge():
    grid = [[5, 3, 1, 0], [4, 1, 1, 3, 2], [2, 3, 2, 4, 3], [0, 2, 3, 3, 2], [1, 0, 2, 4, 3]]
    score = generate_score(grid, 0, 0)
    assert score == 13
