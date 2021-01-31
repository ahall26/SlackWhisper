from decimal import Decimal
import json
import boto3


def load_envariables(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8080")

    table = dynamodb.Table('EnVariables')
    response = table.put_item(Item={"name":"phrasesList","value":str(['error', 'blank page', '404 error', 'not loading', 'having issues', "can't access", 'cancel', 'escalation', 'page down', 'site down', 'slow'])})
    print(response)


load_envariables()
