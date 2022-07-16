from bs4 import BeautifulSoup
import click

import time

from library import compute, driver

@click.command()
@click.option('--url', required=True, type=str, help="Stern Insider Leaderboard **Kiosk** URL")
def main(url):
    scores = dict()
    player_names = list()
     
    webdriver = driver.get_webdriver()
    webdriver.get(url)
    element = driver.wait_for_element_id(webdriver, "shuffle")
    time.sleep(1)

    # run through this twice so we capture the second page of the board
    for x in range(0, 2):
        html = webdriver.page_source
        soup = BeautifulSoup(str(html), 'html.parser')
        div = soup.find("div", {"id": "shuffle"})
        ul = div.find('ul')
        cards = ul.find_all('li', recursive=False)
        for card in cards:
            player_names = list()
            leaderboard_header = card.find("div", {"class": "leaderboard-header"})
            title=leaderboard_header.find('p')
            game_name = title.contents[0]
            # prevent duplicate scores from being added
            if game_name in scores:
                pass
            players = card.find_all('li')
            for player in players:
                name = player.find('p')
                player_name = name.contents[0]
                # don't add dan's scores
                if player_name.lower() != "flex_bt":
                    player_names.append(player_name)

            scores[game_name] = player_names

        time.sleep(9)
    computer = compute.Compute()
    total_scores = computer.get_scores(scores)
    print(total_scores)

if __name__ == "__main__":
    main()