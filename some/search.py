import requests
import urllib
from miniengine import Result

def search(query):
    request_uri = 'https://api.stackexchange.com/2.2/search?'
    formdata = {
            'site': 'stackoverflow',
            'order': 'desc',
            'sort': 'votes',
            'filter': 'default'
            }
    tags = ""
    for keyword in query.keywords:
        if len(tags) > 0:
            tags += ";"
        tags += keyword
    if len(tags) > 0:
        formdata['tagged'] = tags
    if len(query.text) > 0:
        formdata['intitle'] = query.text


    r = requests.get(request_uri + urllib.parse.urlencode(formdata))
    print(r.json())
    results = []
    for item in r.json()['items']:
        res = Result()
        res.title = item['title']
        res.url = item['link']
        res.favicon_url = "https://stackoverflow.com/favicon.ico"
        results.append(res)
    return results


