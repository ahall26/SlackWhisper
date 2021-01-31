import json
from itertools import count, groupby
from collections import Counter 


keywords = ['error', 'blank page', '404 error', 'not loading', 'having issues', "can't access", 'cancel', 'escalation', 'page down', 'site down', 'slow']

with open("responses_slack.json") as json_file:
    events = json.load(json_file)

keywordList = []

for event in events:
    for keyword in keywords:
        if keyword in event['event']['text']:
            event['keyword'] = keyword
            keywordList.append(keyword)

def getKey(item):
     return item[1]

res = sorted(list(set([(el, keywordList.count(el)) for el in keywordList])), key=getKey, reverse=True)

print(res)