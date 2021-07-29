#!/usr/bin/env python3
"""Calculates the likelihood of obtaining this data"""
import numpy as np


def likelihood(x, n, P):
    """
    x: is the number of patients
    n : total number of patients
    P: is 1  numpy.ndarry
    """

    # if n is not int or equl to 0 raise value error inc a msg
    if not(type(n) is int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # if not x is not a int or equal to 0 raise value error with msg
    if not(type(x) is int) or x < 0:

        # im made a message cause of pep8 error
        message = "x must be an integer that is greater than or equal to 0"
        raise ValueError(message)

    # if x is greater than n raise value error inc a msg
    if x > n:
        raise ValueError("x cannot be greater than n")

    # if P is not 1D or P isn"t in range raise a type error inc msg
    if type(P) != np.ndarray or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    for i in P:
        if not (i >= 0 and i <= 1):
            raise ValueError("All values in {P} must be in the range [0, 1]")

    # factorial of n
    fn = np.math.factorial(n)

    # fatorial of x
    fx = np.math.factorial(x)

    # difference between 2 values to calculate
    fs = np.math.factorial(n-x)

    # calc every probability in P
    likelihood = P ** x * (fn / (fx * fs)) * (1-P) ** (n-x)
    return likelihood
