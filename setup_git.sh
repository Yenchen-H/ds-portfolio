#!/bin/bash
# Run this once inside the ds-portfolio folder to push to GitHub.
# Replace YOUR_REPO_URL with your actual GitHub repo URL.
#
# Example:
#   https://github.com/yenchen-h/ds-portfolio.git

REPO_URL="https://github.com/yenchen-h/ds-portfolio.git"

git init
git add .
git commit -m "init: repo structure + L1 Array/LinkedList complete"
git branch -M main
git remote add origin "$REPO_URL"
git push -u origin main

echo "Done. Visit: $REPO_URL"
