import json
import http.client


def lambda_handler(event, context):
    conn = http.client.HTTPSConnection("hooks.slack.com")

    payload = {"text": json.dumps(event)}

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
