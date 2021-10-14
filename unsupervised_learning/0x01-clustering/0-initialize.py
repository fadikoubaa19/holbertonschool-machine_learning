#!/usr/bin/env python3
"""task 0-initialize.py"""
import numpy as np


def initialize(X, k):
    """
    function initialize param:X,K
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None
    if type(k) is not int or k <= 0:
        return None

    o, d = X.shape
    min = np.min(X, axis=0)
    max = np.max(X, axis=0)
    return np.random.uniform(min, max, size=(k, d))
