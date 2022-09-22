#!/usr/bin/env python3
""" displays the upcoming launch with these information:"""
import requests

if __name__ == '__main__':
    data = requests.get('https://api.spacexdata.com/v4/launches/upcoming',
                        headers={'pagination': 'false'})

    data = data.json()
    time = 600000000000
    next = None

    for launch in data:
        now = int(launch['date_unix'])
        if now < time:
            time = now
            next = launch

    if next is not None:
        rocket_name = requests.get('https://api.spacexdata.com/v4/rockets/'
                                   + next['rocket'])

        rocket_name = rocket_name.json()['name']
        pad_name = requests.get('https://api.spacexdata.com/v4/launchpads/'
                                + next['launchpad'])

        # locality of the launchpad
        pad_name = pad_name.json()
        timelocal = pad_name['locality']
        pad_name = pad_name['name']
    # print all formats
    print("{} ({}) {} - {} ({})".format(
        next['name'],
        next['date_local'],
        rocket_name, pad_name,
        timelocal))
