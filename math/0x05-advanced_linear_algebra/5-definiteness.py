#!/usr/bin/env python3
"""function that cal the def of mat"""

import numpy as np


def definiteness(matrix):
    """function defniteness// --> matrix """

    if type(matrix) != np.ndarray:
        raise TypeError("matrix must be a numpy.ndarray")

    if len(matrix.shape) == 1:
        return None

    if not np.array_equal(matrix.T, matrix):
        return None

    chiffer = np.linalg.eigvals(matrix)

    # Test whether all array elements along a given axis evaluate to True.
    if np.all(chiffer < 0):
        return "Negative definite"
    elif np.all(chiffer > 0):
        return "Positive definite"
    elif np.all(chiffer <= 0):
        return "Negative semi-definite"
    elif np.all(chiffer >= 0):
        return "Positive semi-definite"
    else:
        return "Indefinite"
