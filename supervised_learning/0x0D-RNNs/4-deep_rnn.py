#!/usr/bin/env python3
"""
4-deep_rnn.py
"""
import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """
    function deep_rnn: param: rnn_cells, X,h_0:
    performs forward propagation for a deep RNN:
    """

    # Empty lists:
    H = []
    Y = []

    # Add h_0 to empty list H:
    H.append(h_0)

    # giving the legnth of array's dimenstions:
    for j in range(X.shape[0]):

        # Empty list:
        list = []
        h = X[j]
        # Move some elements using forwards method():
        for i in range(len(rnn_cells)):
            h, y = rnn_cells[i].forward(H[j][i], h)

        # aading elements to the empty lists:
            list.append(h)
        H.append(list)
        Y.append(y)

    # Create arrays:
    # H is a numpy.ndarray containing all of the hidden states:
    # Y is a numpy.ndarray containing all of the outputs:
    H = np.array(H)
    Y = np.array(Y)

    # Returns: H, Y:
    return H, Y
