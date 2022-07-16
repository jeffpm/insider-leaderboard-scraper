import pytest

from library import compute

def test_empty_get_scores():
    computer = compute.Compute()
    assert computer.get_scores({}) == dict()

@pytest.mark.parametrize("test_input,expected", 
[
    ({"game0": ["player0"]}, {"player0": 10}),
    ({"game0": ["player0"], "game1": ["player0"]}, {"player0": 20}),
    ({"game0": ["player0", "player1"], "game1":["player1", "player0"]}, {"player0": 18, "player1": 18})
])
def test_getscores(test_input, expected):
    computer = compute.Compute()
    assert computer.get_scores(test_input) == expected

@pytest.mark.parametrize("test_input", 
[
    ({"game0": ["player0", "player1", "player2", "player3", "player4", "player5", "player6", "player7", "player8", "player9"]})
])
def test_points_get_scores(test_input):
    computer = compute.Compute()
    result = computer.get_scores(test_input)
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

def test_sort_scores():
    computer = compute.Compute()
    computer.player_scores = {"player2":5, "player0": 0, "player1":10}
    computer.sort_scores()

    assert list(computer.player_scores.items())[0][0] == "player1"
    assert list(computer.player_scores.items())[1][0] == "player2"
    assert list(computer.player_scores.items())[2][0] == "player0"