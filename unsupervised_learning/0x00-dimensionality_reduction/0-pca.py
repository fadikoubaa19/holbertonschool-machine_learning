#!/usr/bin/env python3
"""
0-pca.py : function that prefrom PCA on data set
"""
import numpy as np


def pca(X, var=0.95):
    """
    X is the nupy of numpy.ndarry of shape (n,d)
    N : number of dara points
    var : the fraction of the varriance
    return : weight matrix, w, var
    w : is numpy.ndarry of shape(d, nd)
    nd : is the demensionality of transformed X
    """

    # variable using numpy(Linear algebre):
    P1, P2, P3 = np.linalg.svd(X)

    # Cumulative sum of P1:
    cum_sum = np.cumsum(P1)
    cum_sum_1 = cum_sum[len(cum_sum) - 1] * var

    # Element indice  btw 2 elements:
    el_indice = np.where(cum_sum_1 > cum_sum)

    # var is the cumulative sum of el_indice
    var = cum_sum[el_indice]
    map = len(var) + 1

    # Return the weight of shape(d, nd) wheere nd is the new dim
    W = P3.T
    ps = W[:, 0:map]
    return ps
