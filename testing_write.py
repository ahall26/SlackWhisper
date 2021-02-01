import json
import http.client


def lambda_handler(event):
    matches = ['error', 'blank page', '404 error', 'not loading', 'having issues', "can't access", 'cancel', 'escalation', 'page down', 'site down', 'slow']
    if any(x in event['event']['text'] for x in matches):
        with open('responses_slack.json') as json_file:
            responses = json.load(json_file)
            
        responses.append(event)
        
        with open('responses_slack.json', 'w') as outfile:
            data = responses
            json.dump(data, outfile)

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
        
        return {
            'statusCode': 200,
            'body': json.dumps(event)
        }
    return None

event = 
lambda_handler(event)