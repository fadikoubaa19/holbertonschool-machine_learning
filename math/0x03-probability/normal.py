#!/usr/bin/env python3
"""Normal module"""


class Normal:
    """new class normal"""
    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        """function init"""
        if data is None:
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
            else:
                self.mean = float(mean)
                self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.mean = sum(data) / len(data)
            s = 0
            for item in data:
                s += (item - self.mean)**2
            self.stddev = (s / len(data))**.5

    def z_score(self, x):
        """function that calculate the x score and z value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """ calculate the x value"""
        return (z * self.stddev) + self.mean
