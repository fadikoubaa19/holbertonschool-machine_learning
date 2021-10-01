#!/usr/bin/env python3
"""function 1-minor"""


def determinant(matrix):
    """
    ---function determinant---
    param: ---> matrix
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    for a in range(len(matrix)):
        if type(matrix[a]) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(matrix) != len(matrix[a]):
            raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    x = 1
    y = 0
    for a in range(len(matrix)):
        copy = []
        for OiO in matrix:
            copy.append(OiO.copy())

        new_matrix = copy[1:]
        for oIo in new_matrix:
            del oIo[a]

        y += matrix[0][a] * determinant(new_matrix) * x
        x = x * -1

    return determinant


def minor(matrix):
    """
    ---Function minor--
    param: --> matrix
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    for a in range(len(matrix)):
        if type(matrix[a]) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(matrix) != len(matrix[a]) or len(matrix[a]) == 0:
            raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    new_list = []
    for a in range(len(matrix)):
        L_L = []
        for OiO in range(len(matrix)):
            copy = []
            for XwX in matrix:
                copy.append(XwX.copy())
            del copy[a]
            for oIo in copy:
                del oIo[OiO]
            L_L.append(determinant(copy))
        new_list.append(L_L)
    return new_list
