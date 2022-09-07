#!/usr/bin/env python3
"""returns the list of names of the home planets of all sentient species"""
import requests


def sentientPlanets():
    """ function sentient planets"""

    url = "https://swapi-api.hbtn.io/api/species"
    planets = []

    while url is not None:
        data = requests.get(url).json()

        for species in data['results']:
            if ((species['designation'] == 'sentient'
                 or species['designation'] == 'reptilian')):
                if species['homeworld'] is not None:
                    datas = requests.get(species['homeworld']).json()
                if datas['name'] not in planets:
                    planets.append(datas['name'])
        url = data['next']
    return planets
