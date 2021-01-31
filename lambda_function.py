import json
import http.client
import boto3


def lambda_handler(event, context=None, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8080")

    matches = dynamodb.Table('EnVariables').scan().get('Items')[0]['value']
    print(matches)

    if any(x in event['event']['text'] for x in matches):
        conn = http.client.HTTPSConnection("hooks.slack.com")
        payload = json.dumps({"text": json.dumps(event,indent=4, sort_keys=True)})
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "4c28ed21-a77f-5d5d-300b-6d33b3813bad"
        }
    
        conn.request(
            "POST", "/services/TM49NLNKU/B01LLFBKHL4/OVUQhnpSx32jJg30m522f4Km", payload, headers)
    
        res = conn.getresponse()
        data = res.read()
    
        print(data.decode("utf-8"))
    
        return {
            'statusCode': 200,
            'body': json.dumps(event)
        }
    return None

with open("response_slack.json") as json_file:
    event = json.load(json_file)
lambda_handler(event)