#!/usr/bin/env python3
"""
adds two matrices element-wise
"""


def add_matrices2D(mat1, mat2):
    """
    2D matrices containing ints/floats
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[mat1[a][i] + mat2[a][i] for i in range(len(mat1[a]))]
            for a in range(len(mat1))]
