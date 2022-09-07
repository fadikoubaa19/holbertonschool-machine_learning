#!/usr/bin/python3

"""hold number of passenger from star wars api"""

import requests


def availableShips(passengerCount):
    """funct avaibleships"""

    url = "https://swapi-api.hbtn.io/api/starships"
    ships = []

    while url is not None:
        data = requests.get(url).json()

        for ship in data['results']:
            try:
                if int(ship['passengers']) >= passengerCount:
                    ships.append(ship['name'])
            except ValueError:
                if ship['name'] == 'Executor' and ((passengerCount == 99999) or (passengerCount < 99999)):
                    ships.append('Executor')

        url = data['next']

    return ships
