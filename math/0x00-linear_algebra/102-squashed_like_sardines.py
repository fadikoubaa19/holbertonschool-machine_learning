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


def cat_matrices(mat1, mat2, axis=0):
    """functio that Concatenates matrices"""
    mat1_a = matrix_shape(mat1)
    mat2_b = matrix_shape(mat2)
    mat1_a.pop(axis)
    mat2_b.pop(axis)
    if mat1_a != mat2_b or axis >= len(mat1) + 1:
        return None
    if axis == 0:
        if isinstance(mat1, list) and isinstance(mat1[0], list):
            n1 = [[a for a in m1] for m1 in mat1]
            n2 = [[b for b in m2] for m2 in mat2]
        else:
            n1 = mat1.copy()
            n2 = mat2.copy()
        return n1 + n2
    else:
        if len(mat1) != len(mat2):
            return None
        return [cat_matrices(c1, c2, axis - 1) for c1, c2 in zip(mat1, mat2)]
