#!/usr/bin/env bash
set -euo pipefail

# Replace with your deployed API URL (no trailing slash!)
API=$(scripts/build_api_url.sh)
API_URL="${API}/hello"


curl "${API_URL}"
echo -e ""

