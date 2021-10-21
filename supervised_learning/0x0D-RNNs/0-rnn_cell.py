#!/usr/bin/env python3
"""0-rnn_cell.py"""

import numpy as np


class RNNCell:
    """
    Create new class RNNcell
    """

    def __init__(self, i, h, o):
        """
        function init:
        param: self, i, h,o
        """

        # Reprensent the instance of variable
        # Create array with normal data:
        self.Wh = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=(h, o))

        # Return a new array of shape:
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        Function forward: self, h_prev, x_t(param):
        """

        # Conc the h_prev & x_t
        x_concat = np.concatenate((h_prev, x_t), axis=1)

        # Return two matrixes products of 2 arrays:
        h_next = np.matmul(x_concat, self.Wh) + self.bh

        # Calculate hyperbolic tangent
        h_next = np.tanh(h_next)

        # Return 2 matrixs products of 2 arrays:
        y = np.matmul(h_next, self.Wy) + self.by

        # Calculate the expenontial:
        y = np.exp(y) / np.sum(np.exp(y), axis=1, keepdims=True)

        return h_next, y
