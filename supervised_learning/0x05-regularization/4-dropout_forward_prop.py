#!/usr/bin/env python3
""" dropout_forward_prop.py"""
import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """conducts forward propagation using Dropout"""

    cache = {}
    cache['A0'] = X
    for layer in range(1, L + 1):
        W = weights['W' + str(layer)]
        b = weights['b' + str(layer)]
        A_prev = cache['A' + str(layer - 1)]
        z = (np.matmul(W, A_prev)) + b
        out = np.random.binomial(1, keep_prob, size=z.shape)

        if layer is L:
            n = np.exp(z)
            cache['A' + str(layer)] = n / np.sum(t, axis=0, keepdims=True)
        else:
            cache['A' + str(layer)] = np.tanh(z)
            cache['D' + str(layer)] = out
            cache['A' + str(layer)] *= out
            cache['A' + str(layer)] /= keep_prob
    return (cache)
