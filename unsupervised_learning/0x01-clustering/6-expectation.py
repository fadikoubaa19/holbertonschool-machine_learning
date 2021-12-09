#!/usr/bin/env python3
"""C6-expectation.py"""
import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """
    function expectation: :calculates the probability density function of a Gaussian distributionparam: x,pu,m,s
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None
    if type(m) is not np.ndarray or len(m.shape) != 2:
        return None, None
    if type(pi) is not np.ndarray or len(pi.shape) != 1:
        return None, None
    if type(S) is not np.ndarray or len(S.shape) != 3:
        return None, None
    n, d = X.shape
    k = pi.shape[0]
    if k > n:
        return None, None
    if d != m.shape[1] or d != S.shape[1] or d != S.shape[2]:
        return None, None
    if k != m.shape[0] or k != S.shape[0]:
        return None, None
    if not np.isclose([np.sum(pi)], [1])[0]:
        return None, None
    cereal = 0
    g = np.zeros((k, n))
    for i in range(k):
        aux = pi[i] * pdf(X, m[i], S[i])
        g[i] = aux
        cereal += aux
    g = g / cereal
    result = np.sum(np.log(cereal))
    return g, result
