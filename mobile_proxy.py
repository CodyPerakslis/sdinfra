import json

def send(status, data):
    return {"statusCode": status, "body": data}

def lambda_handler(event, context):
    return send(200, "Hello, World!")
