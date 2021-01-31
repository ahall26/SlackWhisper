import json
import http.client
import


def lambda_handler(event, context):

    matches = ["slow", "not loading", "page down", "can't access", "having issues"]
    
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
    return none