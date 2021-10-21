#!/usr/bin/env python3
"""
Creates the class RNNCell
"""
import numpy as np


class GRUCell:
    """
    Creating new class named Crucell:that represents a gated recurrent unit.
    param: i,h,o
    """

    def __init__(self, i, h, o):
        """
        Function __init__:Create the public instances
        param: self, i, h,o:
        """

        # Creating public instances:
        # generates normally distributed numbers:
        self.Wz = np.random.normal(size=(i + h, h))
        self.Wr = np.random.normal(size=(i + h, h))
        self.Wh = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=(h, o))

        # Return a (bh,bz,br,by) of given shape and type, filled with zeros:
        self.bh = np.zeros((1, h))
        self.bz = np.zeros((1, h))
        self.br = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        Function forward:performs forward propagation for one time step.
        self, h_prev, x_t:
        """

        # Conc two arrays and joining them in the same shape:
        conc1 = np.concatenate((h_prev, x_t), axis=1)

        # By using matmul ,it will find the matrix product:
        a = np.matmul(conc1, self.Wr) + self.br

        # calc the exp of a:
        a = 1 / (1 + np.exp(-a))

        # find out the product of matrix:
        rs = np.matmul(conc1, self.Wz) + self.bz

        # cal the exp of z:
        rs = 1 / (1 + np.exp(-rs))

        # Conc 2 arrays:
        # h_prev contain the prev hidden state:
        conc2 = np.concatenate((a * h_prev, x_t), axis=1)
        h_next = np.matmul(conc2, self.Wh) + self.bh
        # calc the tang  of h_next using np.tang:
        h_next = np.tanh(h_next)
        h = (1 - rs) * h_prev + rs * h_next

        # Retun the matrix of two array using matmul:
        y = np.matmul(h, self.Wy) + self.by

        # calc the exp of y & x using np.exp:
        # cal the sum using np.sum
        y = np.exp(y) / np.sum(np.exp(y), axis=1, keepdims=True)

        # return h & y (y is the output of cell:
        return h, y
