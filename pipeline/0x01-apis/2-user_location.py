#!/usr/bin/env python3
"""prints the location of a specific user:"""


import requests
import sys
import time


if __name__ == '__main__':
    url = sys.argv[1]

    data = requests.get(url)
    response = data.status_code
    if response == 200:
        print(data.json()['location'])
    elif response == 403:
        reset = data.headers['X-Ratelimit-Reset']
        difference = (int(limit) - int(now)) / 60
        print("Reset in {} min".format(int(difference)))
    else:
        print("Not found")
