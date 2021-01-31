from decimal import Decimal
import json
import boto3

import envariables_insert

def load_phrases(phrases, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8080")

    table = dynamodb.Table('Phrases')   
    for phrase in phrases:
        table.put_item(Item=phrase)

def update_envariables(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8080")

    phrase_list = []
    phrases = dynamodb.Table('Phrases').scan().get('Items',[])

    for phrase in phrases:
        phrase_list.append(phrase['phrase'])          
        print(phrase['phrase'])
    envariables_insert.load_phrases_list(phrase_list)

with open("phrase_data.json") as json_file:
    phrase_list = json.load(json_file, parse_float=Decimal)
load_phrases(phrase_list)
update_envariables()