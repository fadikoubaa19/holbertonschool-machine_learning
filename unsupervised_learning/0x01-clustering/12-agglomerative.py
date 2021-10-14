#!/usr/bin/env python3
"""task 12"""
import scipy.cluster.hierarchy
import matplotlib.pyplot as plt


def agglomerative(X, dist):
    """
    function agglomertive: parm: x,dist
    """
    arc = scipy.cluster.hierarchy
    flat = arc.linkage(y=X, method='ward')
    thecluster = arc.fcluster(Z=flat, t=dist, criterion='distance')
    plt.figure()
    arc.dendrogram(flat, color_threshold=dist)
    plt.show()
    return thecluster
