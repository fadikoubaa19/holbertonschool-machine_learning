#!/usr/bin/env python3
"""function exp"""


class Exponential:
    """distrubute exp
    """
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
    def pmf(self, k):
        """func calc PDF"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        else:
            return (self.lambtha**k * Poisson.e**((-1) * self.lambtha))\
                / Poisson.factorial(k)
