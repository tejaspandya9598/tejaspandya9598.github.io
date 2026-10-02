#!/usr/bin/env bash
# Publish the portfolio. Run from anywhere.
#   ~/Claude/Projects/Applications/portfolio-website/site/deploy.sh "what changed"
set -euo pipefail
cd "$(dirname "$0")"
MSG="${1:-Update portfolio}"
if git diff --quiet && git diff --cached --quiet; then
  echo "No changes to publish."; exit 0
fi
git add -A
git commit -q -m "$MSG"
git push -q origin main
echo "Pushed. GitHub Pages rebuilds in ~30-60s → https://tejaspandya.me"
