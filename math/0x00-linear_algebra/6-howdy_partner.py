#!/usr/bin/env python3
"""
concatenates two arrays
"""


def cat_arrays(arr1, arr2):
    """ function to concat 2 array """
    arr = [i for a in [arr1, arr2] for i in a]
    return arr
