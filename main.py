import json

import get_slack_messages
import phrases_count

get_slack_messages.getMessages()
stats = phrases_count.runGetCount()
for stat in stats:
    print(stat[0],stat[1])
