#!/usr/bin/env python3
"""em.py"""
import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """
    function em: param x,k,ite,tol,verbose
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None, None, None, None
    if type(k) is not int or k <= 0:
        return None, None, None, None, None
    if type(iterations) is not int or iterations <= 0:
        return None, None, None, None, None
    if type(tol) is not float or tol < 0:
        return None, None, None, None, None
    if type(verbose) is not bool:
        return None, None, None, None, None

    begin = 0
    pi, m, S = initialize(X, k)
    g, SSD = expectation(X, pi, m, S)

    for i in range(iterations):
        if verbose and (i % 10 == 0):
            print('Log Likelihood after {} iterations: {}'.
                  format(i, SSD.round(5)))

        pi, m, S = maximization(X, g)
        g, SSD = expectation(X, pi, m, S)

        if abs(begin - SSD) <= tol:
            break
        begin = SSD

    if verbose:
        print('Log Likelihood after {} iterations: {}'
              .format(i + 1, SSD.round(5)))
    return pi, m, S, g, SSD
