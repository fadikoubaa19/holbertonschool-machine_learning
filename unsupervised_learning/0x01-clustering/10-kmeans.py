#!/usr/bin/env python3
"""task 10 is done:"""
import sklearn.cluster


def kmeans(X, k):
    """
    function kmeans: param: x,k
    """
    kmeans = sklearn.cluster.KMeans(n_clusters=k).fit(X)

    C = kmeans.cluster_centers_
    clss = kmeans.labels_

    return C, clss
