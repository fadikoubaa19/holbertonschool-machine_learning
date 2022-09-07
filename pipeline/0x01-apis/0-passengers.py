#!/usr/bin/python
# -*- coding: utf-8 -*-

"""hold number of passenger from star wars api"""

import requests


def availableShips(passengerCount):
    """funct avaibleships"""

    ships = []
    url = 'https://swapi-api.hbtn.io/api/starships'
    while url is not None:
        info = requests.get(url).json()
        for ship in info['results']:
            passengers = ship['passengers'].replace(',', '')
            if passengers == 'n/a' or passengers == 'unknown':
                passengers = -1
            if int(passengers) >= passengerCount:
                ships.append(ship['name'])
        url = info['next']
    return ships
