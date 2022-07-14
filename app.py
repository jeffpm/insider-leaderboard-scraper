from bs4 import BeautifulSoup
import click
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

@click.command()
@click.option('--url', required=True, type=str, help="Stern Insider Leaderboard **Kiosk** URL")
def main(url):
    scores = dict()
    player_names = list()
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "shuffle"))
        )
    time.sleep(1)

    # run through this twice so we capture the second page of the board
    for x in range(0, 2):
        html = driver.page_source
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

    total_scores = compute_scores(scores)
    sorted_total_scores = dict(sorted(total_scores.items(), key=lambda x: x[1], reverse=True))
    print(sorted_total_scores)

if __name__ == "__main__":
    main()