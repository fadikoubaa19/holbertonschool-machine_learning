#!/usr/bin/env python3
"""Calculates the posterior probability of a uniform distribution"""
from scipy import special


def posterior(x, n, p1, p2):
    """
    """
    if not (type(n) is int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not (type(x) is int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")

    # if x is gretaer then n Value error with msg
    if x > n:
        raise ValueError("x cannot be greater than n")

    # if p1 & p2 isn't a float or 0 or 1 value error a msg
    if type(p1) is not float or not 0 <= p1 <= 1:
        raise ValueError("p1 must be a float in the range [0, 1]")
    if type(p2) is not float or not 0 <= p2 <= 1:
        raise ValueError("p2 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")

    beta_1 = special.betainc(x + 1, n - x + 1, p1)
    beta_2 = special.betainc(x + 1, n - x + 1, p2)
    return beta_2 - beta_1
