#!/usr/bin/env python3
""" 2-absorbing.py"""


import numpy as np


def absorbing(P):
    """
    function absorbing: param: p:
    """

    if type(P) is not np.ndarray or len(P.shape) != 2:
        return False
    if np.sum(P, axis=1).all() != 1:
        return None
    n = P.shape[0]
    if n != P.shape[1]:
        return False
    shap = np.shap(P)
    if (shap == 1).all():
        return True
    land = np.where(shap == 1)
    if len(land[0]) == 0:
        return False
    res = shap == 1
    for i in range(n):
        for j in range(n):
            if P[i][j] > 0 and res[j]:
                res[i] = 1
    if res.all() == 1:
        return True
    return False
