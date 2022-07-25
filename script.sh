#!/bin/bash

cd ~/insider-leaderboard-scraper

git fetch origin
git checkout gh-pages
git merge origin/main

pipenv install
pipenv run python app.py --url 'https://insider.sternpinball.com/kiosk/fpdgr-PeKmG-mQW/'

git add -A
timestamp=$(date +%s)
git commit -m timestamp=$(date +%s)

git push --force