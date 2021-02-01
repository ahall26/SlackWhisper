import json

with open('response_slack.json') as json_file:
    response = json.load(json_file)

with open('responses_slack.json') as json_file:
    responses = json.load(json_file)

responses.append(response)

with open('responses_slack.json', 'w') as outfile:
    data = responses
    json.dump(data, outfile)