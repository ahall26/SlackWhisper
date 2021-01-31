from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def scan_phrases(display_phrases, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8080")

    table = dynamodb.Table('Phrases')

    done = False
    start_key = None
    while not done:
        response = table.scan()
        display_phrases(response.get('Items', []))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None


if __name__ == '__main__':
    phrase_list = []
    def print_phrases(phrases):
        for phrase in phrases:
            phrase_list.append(phrase['phrase'])          
            pprint(phrase['phrase'])

    scan_phrases(print_phrases)
    print("Phrases: ", phrase_list)
    print("Number of Phrases: ", len(phrase_list))
