#!/usr/bin/env python3
"""2-variance.py"""
import numpy as np


def variance(X, C):
    """
    function variance: param: x,c
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None
    if type(C) is not np.ndarray or len(C.shape) != 2:
        return None
    if X.shape[1] != C.shape[1]:
        return None

    init = np.square(X - C[:, np.newaxis]).sum(axis=2)
    distances = np.min(init, axis=0)
    result = np.sum(distances)

    return result
