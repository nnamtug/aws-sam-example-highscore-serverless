#!/usr/bin/env bash
set -euo pipefail

output=$(./run_get_topscores.sh)
entries=$(echo "$output" | jq '.result')
count=$(echo "$entries" | jq 'length')

if [ "$count" -ne 10 ]; then
  echo "FAIL: Expected 10 entries, got $count"
  exit 1
fi


# Check ranks: should contain 1 to 10
ranks=$(echo "$entries" | jq '[.[].rank]')
for i in $(seq 1 10); do
  if ! echo "$ranks" | jq ". | index($i)" | grep -q -w '[0-9]'; then
    echo "$output"
    echo ""
    echo "FAIL: Rank $i not found in results"
    exit 1
  fi
done

# Check descending scores
scores=$(echo "$entries" | jq '[.[].score]')
sorted_scores=$(echo "$scores" | jq 'sort_by(-.)')
if [ "$scores" != "$sorted_scores" ]; then
  echo "$output"
  echo ""
  echo "FAIL: Scores are not in descending order"
  exit 1
fi

echo "PASS: Top scores output is valid."
