#!/usr/bin/env python3
"""
1-rnn.py: performs forward propagation for a simple RNN:
"""
import numpy as np


def rnn(rnn_cell, X, h_0):
    """
    function rnn: param:--> rnn_cell,X,h_0:
    """

    # Get the current shape of t,m,i:
    t, m, i = X.shape

    # return to the first dimensions:
    h = h_0.shape[1]
    o = rnn_cell.by.shape[1]
    H = np.zeros((t + 1, m, h))
    Y = np.zeros((t, m, o))
    H[0] = h_0
    for i in range(t):
        x_t = X[i]
        h_prev = H[i]
        h_next, y_next = rnn_cell.forward(h_prev=h_prev, x_t=x_t)
        H[i + 1] = h_next
        Y[i] = y_next

    return H, Y
