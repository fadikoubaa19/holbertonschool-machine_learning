#!/usr/bin/env python3
"""
performs matrix multiplication
"""


def mat_mul(mat1, mat2):
    """
    function that preferom matrix mult
    """
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(x * y for x, y in zip(a, b)) for b in zip(*mat2)]
            for a in mat1]
