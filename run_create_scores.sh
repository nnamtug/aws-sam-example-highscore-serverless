#!/usr/bin/env bash
set -euo pipefail

# Replace with your deployed API URL (no trailing slash!)
API=$(scripts/build_api_url.sh)
API_URL="${API}/score"

# Generate and send 10 random users with scores
for i in $(seq 1 10); do
  user="user$((RANDOM % 1000))"             # random user suffix
  score=$((RANDOM % 10000))                 # random score 0–9999

  echo "Posting score for $user: $score"

  curl -X POST \
    "${API_URL}?username=${user}&score=${score}" \
    -H "Content-Type: application/json"

  echo -e "\n---"
done
