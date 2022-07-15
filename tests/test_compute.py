import pytest

from library import compute

def test_empty_compute_scores():
    assert compute.compute_scores({}) == dict()

@pytest.mark.parametrize("test_input,expected", 
[
    ({"game0": ["player0"]}, {"player0": 10}),
    ({"game0": ["player0"], "game1": ["player0"]}, {"player0": 20}),
    ({"game0": ["player0", "player1"], "game1":["player1", "player0"]}, {"player0": 18, "player1": 18})
])
def test_compute_scores(test_input, expected):
    assert compute.compute_scores(test_input) == expected

@pytest.mark.parametrize("test_input", 
[
    ({"game0": ["player0", "player1", "player2", "player3", "player4", "player5", "player6", "player7", "player8", "player9"]})
])
def test_points_compute_scores(test_input):
    result = compute.compute_scores(test_input)
    assert result["player0"] == 10
    assert result["player1"] == 8
    assert result["player2"] == 7
    assert result["player3"] == 6
    assert result["player4"] == 5
    assert result["player5"] == 4
    assert result["player6"] == 3
    assert result["player7"] == 2
    assert result["player8"] == 1
    assert result["player9"] == 0
