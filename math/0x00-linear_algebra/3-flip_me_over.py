#!/usr/bin/env python3
"""
returns the transpose of a 2D matrix
"""


def matrix_transpose(matrix):
    """
     return a new matrix
    assume all elements in the same dimension
    """
    m = [[matrix[a][b] for a in range(len(matrix))]
         for b in range(len(matrix[0]))]
    while isinstance(matrix, list):
        return m
