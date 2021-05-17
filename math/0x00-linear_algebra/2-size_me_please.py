#!/usr/bin/env python3
"""calculates the shape of a matrix"""


def matrix_shape(matrix):
    """shape that return a list of int"""
    i = [len(matrix)]
    while isinstance(matrix[0], list):
        i.append(len(matrix[0]))
        matrix = matrix[0]
    return i
