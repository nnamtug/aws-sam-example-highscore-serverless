# aws-example-highscore-serverless

A simple serverless backend for a highscore leaderboard built with **AWS SAM**, **API Gateway**, **Lambda**, and **DynamoDB**.  
This project is for experimentation and learning purposes — not production ready. 🚧

---

## Features
- Store scores per user
- Fetch a global leaderboard (top scores across all users)
- Example scripts to build, deploy, seed, and query
- Tear down resources when done

---

## Prerequisites
Before you begin, make sure you have:

- An [AWS account](https://aws.amazon.com/free/) with credentials configured
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- [Docker](https://docs.docker.com/get-docker/) (optional, for local building/emulation)
- Python 3.8+ (tested with 3.13 runtime in Lambda)
- jq, tomlq

---

## Installation & Deployment

1. Check or change the target region in [samconfig.toml](./samconfig.toml)
2. Build the application:
   ```bash
   sam build
   ```

3. Deploy the application:
    ```bash 
    sam deploy
    ```

4. Refresh local resource IDs (helps some helper scripts):
    ```bash
    ./refresh-resourceids.sh
    ```

## Usage
1. Hello World!
    ```bash
    ./run_hello_world.sh
    ```
2. Get current leaderboard 
    ```bash
    ./run_get_topscores.sh
    ```
3. Create random scores 
    ```bash
    ./run_create_scores.sh
    ```
4. Check leaderboard again 
    ```bash
    ./run_get_topscores.sh
    ```

## Tear Down

When you’re done experimenting, clean up resources to avoid charges:
```bash
./delete-stack.sh
```

---
## Notes

- DynamoDB table and API Gateway are pay-per-request, but you may still incur small costs if left running.
- The project is intentionally minimal and insecure (no authentication).
- Use this as a sandbox to learn AWS SAM, not for production workloads.