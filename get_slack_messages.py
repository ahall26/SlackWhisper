import http.client
import json

conn = http.client.HTTPSConnection("slack.com")

headers = {
    'authorization': "Bearer xoxp-718328702674-718331052131-1697750117745-4bae864f471474f43712f419dab8d5de",
    'cache-control': "no-cache",
    'postman-token': "2205480d-30d5-918d-ddbe-2229f626f164"
    }

conn.request("GET", "/api/conversations.history?channel=C01LGD4BA0J&pretty=1", headers=headers)

def getMessages():
    res = conn.getresponse()
    data = res.read()
    ls = []

    with open('responses_slack.json') as json_file:
        responses = json.load(json_file)

    for m in json.loads(data)['messages']:
        x = json.loads(m['text'])
        ls.append(x)

    responses = ls

    with open('responses_slack.json', 'w') as outfile:
        data = responses
        json.dump(data, outfile)