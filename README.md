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

# Updating for a new month
## HTML Template
1. Edit the `index.html` file in the `templates` directory
2. Look for the `<h1>COTU Pinball <month> Leaderboard</h1>` header, and update to the new month.

## Bash script
1. Edit the `script.sh` script and update the Insider Leadeboard Kiosk URL

# Running on a recurring basis

## Setup on device
`sudo apt-get install chromium-chromedriver`

`sudo apt install python3-pip`

`pip install pipenv`

`git config --global user.email "<your_email>"`

1. (cron) clone master
2. (cron) run script
3. (script) checkout gh-pages
4. (script) run python app
5. (script) push changes to gh-pages
