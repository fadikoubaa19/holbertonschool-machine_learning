#!/usr/bin/env python3
""" 1-regular.py """


import numpy as np


def regular(P):
    """
    function regular: param: P
    """

    # P is a is a square 2D:
    if type(P) != np.ndarray:
        return None
    n, m = P.shape
    res = np.ones((1, n)) / m
    check = True

    # [i, j] is the probability of transitioning from state i to state j:
    res = np.matmul(res, P)
    for i in range(n):
        if np.all(P[i]) <= 0:
            return None

    # Returns: a numpy.ndarray of shape (1, n):
    while(check):
        pred = res
        res = np.matmul(res, P)
        if np.all(res == pred):
            return res
