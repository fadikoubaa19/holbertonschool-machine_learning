#!/usr/bin/env python3
"""
concatenates two matrices along a specific axis:
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    function  that conc two matrice
    """
    nlist = []
    if axis == 0 and (len(mat1[0]) == len(mat2[0])):
        return mat1 + mat2
    elif axis == 1 and (len(mat1) == len(mat2)):
        for i in range(len(mat1)):
            newlist = mat1[i] + mat2[i]
            nlist.append(newlist)
        return (nlist)
