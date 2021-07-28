#!/usr/bin/env python3
"""
1-pca.py: Prefom PCA  on a data set
"""
import numpy as np


def pca(X, ndim):
    """
    X is the numpy of shape (n, d)
    n the number of dataset
    d is the number of dimention in each point
    ndim is the new demensionality of the transformed X
    Return  :  T, shape (n, ndim)
    """
    # X the numpy of n darry of shape

    means = X - np.mean(X, axis=0)

    # Using numpy (linear algebre)
    P1, P2, P3 = np.linalg.svd(means)

    W = P3.T
    ps = W[:, 0:ndim]

    T = means @ ps
    return T
