def compute_scores(scores: dict):
    values = [10, 8, 7, 6, 5, 4, 3, 2, 1]
    player_scores = dict()
    for game, players in scores.items():
        for count, player in enumerate(players):
            if player not in player_scores:
                player_scores[player] = 0

            # only add their score if they got any points
            if not count + 1 > len(values):    
                player_scores[player] += values[count]

    return player_scores