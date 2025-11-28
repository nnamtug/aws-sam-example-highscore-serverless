# AGENT INSTRUCTIONS

This repo is an AWS SAM + Python Lambda demo (highscore backend).

## Scope

- These instructions apply to the entire repository.

## General

- Keep changes minimal and focused on the requested task.
- Do not edit generated artifacts:
  - `.aws-sam/**`
  - `.resourceids-*/*`
- Only change `samconfig.toml` stack/region values if explicitly requested.

## Python / Lambda

- Target Python 3.8+ and stay compatible with the Lambda Python 3.13 runtime.
- Prefer standard library; add dependencies only when necessary.
- When adding dependencies, pin them in the relevant `lambda/*/requirements.txt`.
- Keep handlers simple and small; avoid heavy frameworks.

## Infrastructure

- `template.yaml` is the canonical source of infrastructure.
- Preserve existing logical IDs and resource names unless explicitly asked to change them.
- Avoid adding new AWS services or resources unless requested.

## Build & Test

- Build with: `sam build`.
- Use existing scripts for behavior checks:
  - `./run_hello_world.sh`
  - `./run_create_scores.sh`
  - `./run_get_topscores.sh`
  - `./scripts/test_topscores.sh`
- CI/CD is defined in `.github/workflows/deploy-test-destroy.yml`; prefer updating it instead of creating parallel workflows.

## Style

- Prefer clear, explicit Python over clever tricks.
- Do not add new tooling (e.g. Poetry, Makefiles, linters) unless requested.
- Do not add license or copyright headers unless explicitly asked.

