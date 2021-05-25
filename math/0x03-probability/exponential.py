#!/usr/bin/env python3
"""function exp"""


class Exponential:
    """distrubute exp"""

    e = 2.7182818285
    def __init__(self, data=None, lambtha=1.):

        """Initialisation"""
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            else:
                self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = 1 / (sum(data) / len(data))

    def pdf(self, x):
        """func calc PDF"""
        if x < 0:
            return 0
        return self.lambtha * Exponential.e**((-1) * self.lambtha * x)

    def cdf(self, x):
        """func calc PDF"""
        if x < 0:
            return 0
        return 1 - Exponential.e**((-1) * self.lambtha * x)
