#!/usr/bin/env python3
"""
how to add 2 arrays
"""


def add_arrays(arr1, arr2):
    """
    return array
    """
    arr = []
    if len(arr1) == len(arr2):
        for x in range(0, len(arr1)):
            arr.append(arr1[x] + arr2[x])
        return arr
