# Insider Leaderboard Scraper
Uses Selenium + BeautifulSoup to load a Stern Insider Leaderboard Kiosk view, scrape the results, and generate overall standings.

## Pre-requisites
- Python 3.10
- [pipenv](https://pipenv.pypa.io/en/latest/)

## Installation
`pipenv install`

## Running
`pipenv shell`

`pipenv run python app.py --url 'https://insider.sternpinball.com/kiosk/fpdgr-PeKmG-mQW/'`

### See available command line options
`pipenv run python app.py --help`


# Running on a recurring basis


1. (cron) clone master
2. (cron) run script
3. (script) checkout gh-pages
4. (script) run python app
5. (script) push changes to gh-pages