import json
import random

def lambda_handler(event, context):
    random_number = random.randint(1, 100)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "random_number": random_number
        }),
    }
