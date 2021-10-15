#!/usr/bin/env python3
""" 2-absorbing.py"""


import numpy as np


def absorbing(P):
    """
    function absorbing: param: p:
    """

    # P is a is a square 2D numpy.ndarray:
    if type(P) != np.ndarray:
        return None

    # P[i, j] is the probability of transitioning:
    shape = np.diag(P)
    if (shape == 1).all():
        return True
    # if shape = 1 return false:
    if not(shape == 1).any():
        return False

    # the proba of trans P[i,j]:
    if (shape == 1).any():
        for i in range(P.shape[0]):
            for j in range(P.shape[0]):

                # Returns: True if it is absorbing, or False on failure
                if i == j and i + 1 < len(P):
                    if P[i + 1][j] == 0 and P[i][j + 1] == 0:
                        return False
    return True
