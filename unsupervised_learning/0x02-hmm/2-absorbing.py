#!/usr/bin/env python3
""" 2-absorbing.py"""


import numpy as np


def absorbing(P):
    """
    function absorbing: param: p:
    """

    if ((type(P) is not np.ndarray or P.ndim != 2 or
         P.shape[0] != P.shape[1] or np.any(P < 0)
         or not np.all(np.isclose(P.sum(axis=1), 1)))):
        return None

    P = P.copy()
    idx = np.ndarray(P.shape[0])

    while True:
        prev = idx.copy()
        idx = np.any(P == 1, axis=0)

        if idx.all():
            return True

        if np.all(idx == prev):
            return False

        res = np.any(P[:, idx], axis=1)
        P[res, res] = 1
