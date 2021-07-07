#!/usr/bin/env python3
""" dropout_forward_prop.py"""
import numpy as np


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """conducts forward propagation using Dropout"""

    cache = {}
    cache['A0'] = X
    for i in range(1, j + 1):
        w = weights['W' + str(i)]
        b = weights['b' + str(i)]
        c = cache['A' + str(i - 1)]
        n = (np.matmul(w, c)) + b
        dropout = np.random.binomial(1, keep_prob, size=n.shape)

        if i is j:
            t = np.exp(n)
            cache['A' + str(i)] = t / np.sum(t, axis=0, keepdims=True)
        else:
            cache['A' + str(i)] = np.tanh(n)
            cache['D' + str(i)] = dropout
            cache['A' + str(i)] *= dropout
            cache['A' + str(i)] /= keep_prob
    return (cache)
