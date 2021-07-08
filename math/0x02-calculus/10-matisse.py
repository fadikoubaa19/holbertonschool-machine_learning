#!/usr/bin/env python3
"""s """


def poly_derivative(poly):

    """function that Calculates the der of ply"""

    if poly == [] or type(poly) != list or len(poly) == 0:
        return None

    for clss in poly:
        if not isinstance(clss, (int, float)):
            return None

    if len(poly) == 1:
        return [0]

    d = []
    for x in range(len(poly)):
        d.append(poly[x] * x)
    return d[1:]
