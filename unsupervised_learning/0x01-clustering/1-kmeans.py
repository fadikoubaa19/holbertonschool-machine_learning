#!/usr/bin/env python3
"""1-Kmeans.py"""
import numpy as np


def kmeans(X, k, iterations=1000):
    """
    function kmeans: param:X,K,iterations:
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return (None, None)
    if type(k) is not int or k <= 0:
        return (None, None)
    if type(iterations) is not int or iterations <= 0:
        return (None, None)

    o, d = X.shape
    min = np.min(X, axis=0)
    max = np.max(X, axis=0)
    vari = np.random.uniform(min, max, size=(k, d))

    for i in range(iterations):
        copy = vari.copy()
        ins = np.linalg.norm((X - vari[:, np.newaxis]), axis=2)
        init = ins.argmin(axis=0)
        for j in range(k):
            if (X[init == j].size == 0):
                vari[j] = np.random.uniform(min, max, size=(1, d))
            else:
                vari[j] = (X[init == j].mean(axis=0))
                
        # calculate one of the eight different matrix norms or vector norms:
        ins = np.linalg.norm((X - vari[:, np.newaxis]), axis=2)
        init = ins.argmin(axis=0)
        if (copy == vari).all():
            break

    return vari, init
