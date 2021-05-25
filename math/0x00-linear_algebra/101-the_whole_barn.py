#!/usr/bin/env python3
"""function that add two matrices"""


def matrix_shape(matrix):
    """a function that find the shape of matrice"""
    def shape(m, size=None):
        """Finds the shape of matrix recursively"""
        if size is None:
            size = []
        if type(m) is not list:
            return size
        else:
            size.append(len(m))
            return shape(m[0], size)
    return shape(matrix)


def add_matrices(mat1, mat2):
    """function that adds 2 matrices in new one"""
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    if len(matrix_shape(mat1)) > 1:
        return [add_matrices(mat1[i], mat2[i]) for i in range(len(mat1))]
    else:
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
