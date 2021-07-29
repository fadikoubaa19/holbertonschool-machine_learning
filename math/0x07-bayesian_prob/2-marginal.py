#!/usr/bin/env python3
"""1-main.py"""
import numpy as np


def intersection(x, n, P, Pr):
    """
    x: is the number of patients
    n : total number of patients
    P: is 1  numpy.ndarry
    """

    # if n is not n or equal to 0 raise value error
    if not(type(n) is int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # if x is not int or equal to 0 raise value error
    if not(type(x) is int) or x < 0:
        raise ValueError(
            'x must be an integer that is greater than or equal to 0')

    # if x is greater then n raise value eror
    if x > n:
        raise ValueError("x cannot be greater than n")

    # if p is not 1D in np.ndarry or not 1 raise value eror
    if type(P) != np.ndarray or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    # if pr isnot 1D in np.ndarry or pr in not in range raise value error
    if type(Pr) != np.ndarray or P.shape != Pr.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    for idx in P:
        if not (idx >= 0 and idx <= 1):
            raise ValueError("All values in P must be in the range [0, 1]")
    for idx in Pr:
        if not (idx >= 0 and idx <= 1):
            raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    # factorial of n
    fn = np.math.factorial(n)

    # factorial of x
    fx = np.math.factorial(x)

    # factorial of diff btw n & x
    fs = np.math.factorial(n-x)

    likeilhood = P ** x * (fn / (fx * fs)) * (1-P) ** (n-x)
    return likeilhood * Pr


def marginal(x, n, P, Pr):
    """
    function to calc the sum
    """
    return np.sum(intersection(x, n, P, Pr))
