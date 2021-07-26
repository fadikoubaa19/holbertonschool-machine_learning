#!/usr/bin/env python3
"""function that calculates a correlation matrix"""
import numpy as np


def correlation(C):
    """
    function correlation(C)
    C is the shape (d,d) that contains cova matrix
    C in 2 cases:
    if C isn't numpy raise type error + message
    if C does not have shape raise a value error
    return : the correlation
    """
    # if c is not np raise type error
    if type(C) is not np.ndarray:
        raise TypeError("C must be a numpy.ndarray")

    # if C does not have shape raise a Value error
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    stdr = np.sqrt(np.diag(C))

    out_st = np.outer(stdr, stdr)

    correlation = C / out_st

    # return correlation , the numpy of shape that contain the correlation
    correlation[C == 0] = 0
    return correlation
