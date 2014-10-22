import json
import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    return data["topartists"]["artist"][0]["name"]


if __name__ == "__main__":
    # url should be the url to the last.fm api call which
    # will return find the top artists in Spain
    
    url = "http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&" + \
      "country=spain&api_key=880bdf60f4bb7dc2d2668630c8890547&format=json"
    print api_get_request(url)
