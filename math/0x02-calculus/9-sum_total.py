#!/usr/bin/env python3
"""sum_total.py"""


def summation_i_squared(n):
    """
    Function that calc the sum of square
    """
    if n != int and n <= 0:
        return None
    else:
        total = sum((map(lambda total: total ** 2, range(1, n+1))))
        return total
