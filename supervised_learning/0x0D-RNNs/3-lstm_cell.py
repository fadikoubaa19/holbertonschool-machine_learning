#!/usr/bin/env python3
"""
3-lstm_cell.py
"""
import numpy as np


class LSTMCell:
    """
    new class LSTMCell: represent the weights and biases of the cel.
    """

    def __init__(self, i, h, o):
        """
        """

        # Wfand bf are for the forget gate
        self.Wf = np.random.normal(size=(i + h, h))

        # Wuand bu are for the update gate:
        self.Wu = np.random.normal(size=(i + h, h))

        # Wuand bu are for the update gate:
        self.Wc = np.random.normal(size=(i + h, h))

        # Wcand bc are for the intermediate cell state:
        # Woand bo are for the output gate:
        # Wyand by are for the outputs:
        self.Wo = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=(h, o))

        # Return a new array of given shape and type, filled with zeros:
        self.bf = np.zeros((1, h))
        self.bu = np.zeros((1, h))
        self.bc = np.zeros((1, h))
        self.bo = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, c_prev, x_t):
        """
        Function forward:
        param: self, h_prev, c_prev, x_t:
        """

        # join two or more arrays of the same shape along:
        conc1 = np.concatenate((h_prev, x_t), axis=1)
        pro = np.matmul(conc1, self.Wf) + self.bf
        pro = 1 / (1 + np.exp(pro))
        lm = np.matmul(conc1, self.Wu) + self.bu
        mt = 1 / (1 + np.exp(-lm))
        i = np.matmul(conc1, self.Wc) + self.bc

        # Compute hyperbolic tangent of i:
        i = np.tanh(i)

        # Return the matrice product of ab:
        ab = np.matmul(conc1, self.Wo) + self.bo

        # calca ab exp:
        ab = 1 / (1 + np.exp(-ab))

        # c_next is the next cell state:
        c_next = (lm * i) + (pro * c_prev)
        h_t = ab * np.tanh(c_next)

        # return the matrice of product y:
        y = np.matmul(h_t, self.Wy) + self.by

        # calc exp of y using np.exp:
        y = np.exp(y) / np.sum(np.exp(y), axis=1, keepdims=True)

        # y is the output of the cell
        return h_t, c_next, y
