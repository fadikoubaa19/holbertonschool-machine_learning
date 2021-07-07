#!/usr/bin/env python3
""" dropout_forward_prop.py"""
import numpy as np


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """conducts forward propagation using Dropout"""

    weigh_w = weights.copy()
    rt = cache["A" + str(L)] - Y
    m = len(Y[0])
    for i in range(L, 0, -1):
        b = "b" + str(i)
        w = "W" + str(i)
        d = "D" + str(i - 1)
        Actv = cache["A" + str(i - 1)]
        s_1 = (1 / m) * np.sum(rt, axis=1, keepdims=True)
        s_2 = (1 / m) * np.matmul(rt, Actv.T)
        weights[w] = weights[w] - alpha * s_2
        weights[b] = weights[b] - alpha * s_1
        cl = 1 - Actv * Actv
        if i > 1:
            rt = np.matmul(weigh[w].T, rt) * cl * cache[d] / keep_prob
