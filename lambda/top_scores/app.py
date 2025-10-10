import boto3
import json
import os

from boto3.dynamodb.conditions import Key

from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table_name = os.environ["HIGHSCORE_TABLE_NAME"]
table = dynamodb.Table(table_name)

def decimal_default(obj):
    if isinstance(obj, Decimal):
        # keep integers as int; non-integers as float
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

def get_top_scores(limit: int = 10):
    response = table.query(
        IndexName="LeaderboardByScore",
        KeyConditionExpression=Key("LeaderboardPK").eq("LEADERBOARD"),
        ScanIndexForward=False,  # descending by score
        Limit=limit
    )

    return response["Items"]

def lambda_handler(event, context):
    allowed = os.environ.get('CORS_ALLOWED', '').split(',')

    if event.get('httpMethod') == "OPTIONS":
        return options(allowed)
    
    item_dto = get_top_scores()

    # Add rank field (starting at 1)
    for idx, entry in enumerate(item_dto, start=1):
        entry["rank"] = idx

    response = {
        "result": item_dto
    }

    return {
        "statusCode": 200,
        "headers": headers(allowed),
        "body": json.dumps(response, default=decimal_default)
    }   

def options(allowed):
    return {
        "statusCode": 204,
        "headers": headers(allowed)
    }

def headers(allowed):
    return {
        "Access-Control-Allow-Origin": " ".join(allowed),
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
    }
