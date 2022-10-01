#!/bin/bash
set -e

cd ~/insider-leaderboard-scraper

git fetch origin
git checkout gh-pages
git stash push --include-untracked
git merge -X ours origin/main --no-commit

/usr/local/bin/pipenv install --skip-lock
/usr/local/bin/pipenv run python app.py --url 'https://insider.sternpinball.com/insider/leaderboards/iMBr-EAcD-PJUM'
git add -A
timestamp=$(date +%s)
git commit -m timestamp=$(date +%s)

git push --force
