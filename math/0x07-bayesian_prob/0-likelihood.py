#!/usr/bin/env python3
"""Calculates the likelihood of obtaining this data"""
import numpy as np


def likelihood(x, n, P):
    """
    x: is the number of patients
    n : total number of patients
    P: is 1  numpy.ndarry
    """

    if not(type(n) is int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not(type(x) is int) or x < 0:
        msg = "x must be an integer that is greater than or equal to 0"
        raise ValueError(msg)
    if x > n:
        raise ValueError("x cannot be greater than n")
    if type(P) != np.ndarray or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    for i in P:
        if not (i >= 0 and i <= 1):
            msg = "All values in P must be in the range [0, 1]"
            raise ValueError(msg)
    # factorial of n
    fn = np.math.factorial(n)

    # fatorial of x
    fx = np.math.factorial(x)

    # difference between 2 values to calculate
    fs = np.math.factorial(n-x)

    # calc every probability in P
    likelihood = P ** x * (fn / (fx * fs)) * (1-P) ** (n-x)
    return likelihood
