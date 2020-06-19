import json

import requests


def get_location_id(query):
    url = 'https://www.compass.com/api/v3/omnisuggest/autocomplete'
    body = {
        "q": query,
        "sources": [1, 24, 2, 5, 3],
        "listingTypes": [2],
        "limit": 20}
    headers = {
        'Host': 'www.compass.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        "Referer": "https://www.compass.com/agents/search-results/",
        "content-type": "application/json",
    }
    r = requests.post(url, data=json.dumps(body), headers=headers)
    pretty_data = json.loads(r.text)
    if "categories" not in pretty_data.keys():
        return False
    else:
        return pretty_data["categories"][0]["items"][0]["id"]

if __name__ == "__main__":
    mine = get_location_id("08629")
