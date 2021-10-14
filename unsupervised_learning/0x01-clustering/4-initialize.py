#!/usr/bin/env python3
"""4-initialize.py"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """
    function initialize: param: x,k
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None, None
    if type(k) is not int or k <= 0:
        return None, None, None
    n, d = X.shape
    m, _ = kmeans(X, k)
    pi = np.ones(k) / k
    S = np.tile(np.identity(d), (k, 1)).reshape((k, d, d))
    return pi, m, S
