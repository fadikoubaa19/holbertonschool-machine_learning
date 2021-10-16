#!/usr/bin/env python3
"""0-gp.py"""
import numpy as np


class GaussianProcess:
    """gaussian class"""

    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        """
        function init:pram: self, x init,y init...
        """
        self.X = X_init

        self.Y = Y_init

        self.l = l

        self.sigma_f = sigma_f

        self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        """function kernel"""
        return pow(self.sigma_f, 2) * np.exp(pow(X1 - X2.T, 2) /
                                             -2 / pow(self.l, 2))

    def predict(self, X_s):
        """
        function predict
        """
        K = self.kernel(self.X, self.X)
        K_s = self.kernel(self.X, X_s)
        K_m = self.kernel(X_s, X_s)
        K_x = np.linalg.inv(K)

        nud_s = K_s.T.dot(K_x).dot(self.Y)

        ls_s = K_m - K_s.T.dot(K_x).dot(K_s)
        cd_s = ls_s.diagonal()
        return nud_s.reshape(-1), cd_s
