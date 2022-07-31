class Compute:
    def __init__(self):
        self.player_scores = dict()

    def compute_scores(self, scores: dict):
        values = [10, 8, 7, 6, 5, 4, 3, 2, 1]
        player_scores = dict()
        for game, players in scores.items():
            for count, player in enumerate(players):
                if player not in player_scores:
                    player_scores[player] = 0

                # only add their score if they got any points
                if not count + 1 > len(values):    
                    player_scores[player] += values[count]
        self.player_scores = player_scores
    
    def sort_scores(self):
        self.player_scores = dict(sorted(self.player_scores.items(), key=lambda x: x[1], reverse=True))

    def get_scores(self, scores: dict):
        self.compute_scores(scores)
        self.sort_scores()

        return self.player_scores

    def get_scores_list(self):
        scores_list = list()
        scores_list.append(("place", "name", "points"))
        for count, (name, score) in enumerate(self.player_scores.items()):
            if score > 0:
                scores_list.append((count + 1, name, score))

        return scores_list
