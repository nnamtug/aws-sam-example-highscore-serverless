#!/usr/bin/env bash
set -euo pipefail

# Get absolute path of the directory containing this script
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

stackname=$(tomlq '.default.global.parameters.stack_name' ${script_dir}/../samconfig.toml | jq -r)


resourcedir="/.resourceids-${stackname}"
echo $resourcedir