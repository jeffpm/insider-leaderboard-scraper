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
@click.option('--url', required=True, type=str, help="Stern Insider Leaderboard URL")
@click.option('--email', default='dwfarrell@gmail.com', show_default=True, required=True, type=str, help='Stern Insider Email')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=False, help='Stern Insider Password')
def main(url, email, password):
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://insider.sternpinball.com/login')

    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )

    

    driver.find_element("xpath", '//*[@id="email"]').send_keys(email)
    driver.find_element("xpath", '//*[@id="password"]').send_keys(password)
    driver.find_element("xpath", '//*[@id="root"]/div/div[1]/div/div/div/div/div/form/button').click()
    
    time.sleep(5)
    # element = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.ID, "root"))
    # )
    
    driver.get(url)
    # driver.get('https://insider.sternpinball.com/insider/events/fpdgr-PeKmG-mQW?location=1015&fbclid=IwAR3K75mPtWN1-WxgSgFOAtQf3lup7Kga7yl9fZC-bXM_JloEbLOvTERP9t4')
    time.sleep(5)


    scores = dict()
    players = list()

    html = driver.page_source
    soup = BeautifulSoup(str(html), 'html.parser')
    div = soup.find("div", {"id": "shuffle"})
    ul = div.find('ul')

    # machine names and scores show up as list items under the first unsorted list
    # so we'll parse those to get scores
    for count, li in enumerate(ul.find_all('li')):
        text = li.find('p').contents[0]
        # all machine names include "High Scores" in the text
        # so we'll key off that to determine if the item is a machine name
        if "high scores" in text.lower():
            game = text
            # if there are players in the list, the prior game is complete
            # so add the player list to the scores dict
            if len(players) != 0:
                scores[game] = players
            players = list()
    
        # otherwise, it's a player, so we add them to the list
        else:
            # dont include Dan in the scores
            if text.lower() != "flex_bt":
                players.append(text)

        # once we reach this point, it's the last player in the list
        # so we add the list to scores dict
        scores[game] = players

    total_scores = compute_scores(scores)
    sorted_total_scores = dict(sorted(total_scores.items(), key=lambda x: x[1], reverse=True))
    print(sorted_total_scores)

if __name__ == "__main__":
    main()