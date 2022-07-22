from app.schemas.scores import Score, Scores


def test_score():
    score = Score(x=0, y=1, score=20)
    assert score.x == 0
    assert score.y == 1
    assert score.score == 20


def test_scores():
    score_one = Score(x=0, y=0, score=10)
    score_two = Score(x=0, y=1, score=20)
    score_three = Score(x=0, y=3, score=15)

    score_list = Scores(scores=[])
    score_list.scores.append(Score(**score_one.dict()))
    score_list.scores.append(Score(**score_two.dict()))
    score_list.scores.append(Score(**score_three.dict()))

    score_list = score_list.dict()['scores']
    assert score_list[0]['x'] == 0
