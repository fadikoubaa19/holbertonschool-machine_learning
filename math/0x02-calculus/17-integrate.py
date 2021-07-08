#!/usr/bin/env python3
"""integrate.py"""


def poly_integral(poly, C=0):

    """ function that Calculates the integral"""
    if type(poly) != list or len(poly) == 0 or poly is None:
        return None

    if type(C) not in (int, float) or C is None:
        return None

    if poly == [0]:
        return [C]

    ints = [C]
    for x in range(len(poly)):
        result = poly[x] / (x + 1)
        if result.is_integer():
            result = int(result)
        ints.append(result)
    return ints
