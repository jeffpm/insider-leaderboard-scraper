#!/bin/bash
set -e

cd ~/insider-leaderboard-scraper

git fetch origin
git checkout gh-pages
git merge -X ours origin/main --no-commit

/usr/local/bin/pipenv install --skip-lock
/usr/local/bin/pipenv run python app.py --url 'https://insider.sternpinball.com/kiosk/fpdgr-PeKmG-mQW/'

git add -A
timestamp=$(date +%s)
git commit -m timestamp=$(date +%s)

git push --force
