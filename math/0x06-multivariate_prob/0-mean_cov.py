#!/usr/bin/env python3
"""calculates the mean and covariance of a data set"""
import numpy as np


def mean_cov(X):
    """n is number of data points
       if x not 2D raise error
       reurn:means ,cov
       mean caintain the mean of data set
       cov contain the covriance matrix of data set
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    if X.shape[0] < 2:
        raise ValueError("X must contain multiple data points")

    n, d = X.shape

    mean = np.mean(X, axis=0).reshape(1, d)
    int = X - mean
    cov = np.dot(int.T, int) / (n - 1)
    return mean, cov
