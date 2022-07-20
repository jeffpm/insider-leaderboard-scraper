from bs4 import BeautifulSoup

import logging

class Insider:
    def __init__(self):
        self.scores = dict()

    def parse_leaderboard(self, html):
        soup = BeautifulSoup(str(html), 'html.parser')
        div = soup.find("div", {"id": "shuffle"})
        ul = div.find('ul')
        cards = ul.find_all('li', recursive=False)

        for card in cards:
            player_names = list()
            leaderboard_header = card.find("div", {"class": "leaderboard-header"})
            title=leaderboard_header.find('p')
            game_name = title.contents[0]
            logging.debug(f"found game {game_name}")
            # prevent duplicate scores from being added
            if game_name in self.scores:
                pass
            players = card.find_all('li')
            for player in players:
                name = player.find('p')
                player_name = name.contents[0]
                logging.debug(f"found player {player_name}")
                # don't add dan's scores
                if player_name.lower() != "flex_bt":
                    player_names.append(player_name)

            self.scores[game_name] = player_names
            logging.debug(f"scores: {self.scores}")
    def get_scores(self):
        return self.scores