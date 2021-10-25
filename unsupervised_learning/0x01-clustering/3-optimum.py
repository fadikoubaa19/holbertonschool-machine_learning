#!/usr/bin/env python3
"""3-optimum.py"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """
    function optimum:tests for the optimum number of clusters by variance:parm:x,kmin,kmax,iterations:
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None
    if type(kmin) is not int or kmin < 1:
        return None, None
    if kmax is not None and (type(kmax) is not int or kmax < 1):
        return None, None
    if kmax is not None and kmin >= kmax:
        return None, None
    if type(iterations) is not int or iterations < 1:
        return None, None

    n, o = X.shape
    if kmax is None:
        kmax = n

    results = []
    clus = []
    for a in range(kmin, kmax + 1):
        init, classes = kmeans(X, a, iterations)
        results.append((init, classes))

        if a == kmin:
            inis = variance(X, init)
        ex = variance(X, init)
        clus.append(inis - ex)

    return results, clus
