import re
import requests as req
import json
import urllib

with open('topics.json', 'r') as f:
    topicsFile = json.load(f)

topics = topicsFile['topics']

ranks = dict()

for topic in topics:
    url = 'https://www.google.com/search?source=hp&ei=1re-W86tDYSotQWi7LCICw&q=' + \
        urllib.quote_plus(topic)
    request = req.get(url).text.encode("utf-8")

    # print(request.text.encode("utf-8"))
    result = re.findall('resultStats"\>.*de (\d.*) resultados\<div',
                        request)
    # print(url)
    print(result)
