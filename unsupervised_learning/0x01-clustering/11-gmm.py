#!/usr/bin/env python3
"""task 11 is done"""
import sklearn.mixture


def gmm(X, k):
    """
    function gmm: param: x,k
    """
    fat = sklearn.mixture.GaussianMixture(n_components=k)
    fat.fit(X)

    pi = fat.weights_
    m = fat.means_
    S = fat.covariances_

    clss = fat.predict(X)
    bic = fat.bic(X)

    return pi, m, S, clss, bic
