import requests
import json


def jokes(f):
    data = requests.get(f)
    ans = json.loads(data.text)


    return ans