import boto3
import json
import os
import time

dynamodb = boto3.resource("dynamodb")
table_name = os.environ["HIGHSCORE_TABLE_NAME"]
table = dynamodb.Table(table_name)

def save_score(user: str, score: int):
    # Each score item also needs LeaderboardPK for the GSI
    item = {
        "user": user,
        "score": score,
        "LeaderboardPK": "LEADERBOARD",
        "created_at": int(time.time())  # optional timestamp
    }
    table.put_item(Item=item)
    return item

def lambda_handler(event, context):
    allowed = os.environ.get("CORS_ALLOWED", "").split(",")

    method = event.get("httpMethod")

    if method == "OPTIONS":
        return options(allowed)

    if method == "POST":
        params = event.get("queryStringParameters") or {}
        user = params.get("username")
        score_str = params.get("score")

        if not user or not score_str:
            return {
                "statusCode": 400,
                "headers": headers(allowed),
                "body": json.dumps({"error": "username and score are required query parameters"})
            }

        try:
            score = int(score_str)
        except ValueError:
            return {
                "statusCode": 400,
                "headers": headers(allowed),
                "body": json.dumps({"error": "score must be an integer"})
            }

        item = save_score(user, score)
        return {
            "statusCode": 200,
            "headers": headers(allowed),
            "body": json.dumps({"message": "score saved", "item": item})
        }

    return {
        "statusCode": 405,
        "headers": headers(allowed),
        "body": json.dumps({"error": f"Method {method} not allowed"})
    }

def options(allowed):
    return {
        "statusCode": 204,
        "headers": headers(allowed)
    }

def headers(allowed):
    return {
        "Access-Control-Allow-Origin": " ".join(allowed),
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
    }
