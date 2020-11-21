import requests
import urllib
from miniengine import Result, cachedrequest

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

    request_uri += urllib.parse.urlencode(formdata)
    r = cachedrequest(request_uri)
    results = []
    for item in r['items']:
        res = Result()
        res.title = item['title']
        res.url = item['link']
        res.favicon_url = "https://stackoverflow.com/favicon.ico"
        res.score = item['score']
        results.append(res)
    return results
