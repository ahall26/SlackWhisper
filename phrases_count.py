import json


keywords = ['error', 'blank page', '404 error', 'not loading', 'having issues', "can't access", 'cancel', 'escalation', 'page down', 'site down', 'slow']
keywordList = []

def getKey(item):
     return item[1]

def getCount():
    with open("responses_slack.json") as json_file:
        events = json.load(json_file)

    for event in events:
        for keyword in keywords:
            if keyword in event['event']['text']:
                keywordList.append(str(keyword).capitalize())

    res = sorted(list(set([(el, keywordList.count(el)) for el in keywordList])), key=getKey, reverse=True)

    return res

def runGetCount():
    with open('requests.json', 'w') as outfile:
        data = getCount()
        print("Aggregated List",data)
        json.dump(data, outfile)
    return data