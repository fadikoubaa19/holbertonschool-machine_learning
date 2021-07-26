#!/usr/bin/env python3
""" function that  that calculates the PDF at a data point"""
import numpy as np


class MultiNormal():
    """New class constructor"""
    def __init__(self, data):
        """
        n is number of data
        d number of dimensions in each data point
        mean is the mean of data
        cov is the covariance matrix data
        """

        # if data not 2D raise Typeerror includded with msg
        if type(data) is not np.ndarray or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        # if n is less then 2 raise Value error includded with msg
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")

        # Initialiation
        d, n = data.shape

        self.mean = np.mean(data, axis=1).reshape(d, 1)

        int = data - self.mean

        self.cov = np.dot(int, int.T) / (n - 1)
