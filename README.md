# aws-example-hiscore-serverless
Serverless backend for a highscore table. Just to fool around. Not production ready.


## Prerequisites
- Get an AWS Account
- Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Install [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- Have docker installed to build (optional, but reasonable)
- Have python3 installed


## Install
1. Check/change region in [samconfig.toml](./samconfig.toml)
2. ```sam build```
3. ```sam deploy```
4. ```./refresh-resourceids.sh```

## Play
1. ```./run_hello_world.sh```
2. ```./run_get_topscores.sh```
3. ```./run_create_scores.sh```
4. ```./run_get_topscores.sh```

## Tear Down
```./delete-stack.sh```