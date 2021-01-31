from decimal import Decimal
import json
import boto3


def load_phrases(phrases, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8080")

    table = dynamodb.Table('Phrases')   
    for phrase in phrases:
        print(phrase)
        response = table.put_item(Item=phrase)
        print(response)


with open("phrase_data.json") as json_file:
    phrase_list = json.load(json_file, parse_float=Decimal)
load_phrases(phrase_list)
