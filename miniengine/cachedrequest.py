import requests

cached_requests = dict()

def cachedrequest(url):
    if url in cached_requests:
        return cached_requests[url]
    r = requests.get(url).json()
    cached_requests[url] = r
    return r
