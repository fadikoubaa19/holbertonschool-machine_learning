#!/usr/bin/env python3
"""5-pdf.py"""
import numpy as np


def pdf(X, m, S):
    """
    function pdf: param: x,m,S
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None
    if type(m) is not np.ndarray or len(m.shape) != 1:
        return None
    if type(S) is not np.ndarray or len(S.shape) != 2:
        return None
    if X.shape[1] != m.shape[0] or X.shape[1] != S.shape[0]:
        return None
    if S.shape[0] != S.shape[1]:
        return None
    n, d = X.shape
    a = np.linalg.det(S)
    b = np.linalg.inv(S)
    c = 1 / np.sqrt((2 * np.pi) ** d * a)
    firstsplit = np.matmul((-(X - m) / 2), b)
    secondsplit = np.matmul(firstsplit, (X - m).T).diagonal()
    mult = np.exp(secondsplit)
    result = mult * c
    P = np.where(result < 1e-300, 1e-300, result)
    return P
