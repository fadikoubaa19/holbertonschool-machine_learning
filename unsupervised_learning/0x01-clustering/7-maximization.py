#!/usr/bin/env python3
"""task 7 is done"""
import numpy as np


def maximization(X, g):
    """
    function maximization; param; X,g
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None, None
    if type(g) is not np.ndarray or len(g.shape) != 2:
        return None, None, None
    if X.shape[0] != g.shape[1]:
        return None, None, None
    posterior = np.sum(g, axis=0)
    posterior = np.sum(posterior)
    if (int(posterior) != X.shape[0]):
        return (None, None, None)
    n, d = X.shape
    k, o = g.shape
    smooth = np.sum(g, axis=1)
    pi = smooth / n
    HDD = np.zeros((k, d))
    SSD = np.zeros((k, d, d))
    for i in range(k):
        ven = g[i].reshape(1, -1)
        sweet = smooth[i]
        HDD[i] = np.dot(ven, X) / sweet
        begin = ven * (X - HDD[i]).T
        SSD[i] = np.dot(begin, (X - HDD[i])) / sweet
    return pi, HDD, SSD
