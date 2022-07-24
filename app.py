from bs4 import BeautifulSoup
import click
from jinja2 import Environment, FileSystemLoader
import tabulate

import logging
import os
import time

from library import compute, driver, website, insider

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

@click.command()
@click.option('--url', required=True, type=str, help="Stern Insider Leaderboard **Kiosk** URL")
@click.option('--num-pages', required=True, default=2, type= int, help="Number of pages in the leaderboard")
def main(url, num_pages):
    scores = dict()
    player_names = list()
     
    webdriver = driver.Driver()
    logging.debug("loading leaderboard")
    webdriver.get_webdriver().get(url)
    logging.debug("waiting for leaderboard to show")
    webdriver.wait_for_element_id("shuffle")
    time.sleep(1)

    sterninsider = insider.Insider()
    
    logging.info(f"running through {num_pages} leaderboard pages")
    for x in range(0, num_pages):
        html = webdriver.get_webdriver().page_source
        sterninsider.parse_leaderboard(html)
        wait_counter = 0
        while webdriver.get_webdriver().page_source == html:   
            time.sleep(1)
            wait_counter += 1
            if wait_counter == 20:
                logging.warning("wait timeout reached")
                break

    scores = sterninsider.get_scores()
    computer = compute.Compute()
    total_scores = computer.get_scores(scores)
    logging.info(f"scores: {total_scores}")
    scores_list = computer.get_scores_list()

    website.make_leaderboard_page(scores_list)

    

if __name__ == "__main__":
    main()