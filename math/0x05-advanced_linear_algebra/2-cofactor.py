#!/usr/bin/env python3
"""Calculates the cofactor matrix of a matrix"""


def determinant(matrix):
    """
    --Function determiant--
    param:
    --> matrix
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(matrix) != len(matrix[i]):
            raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    x = 1
    y = 0
    for i in range(len(matrix)):
        copy = []
        for element in matrix:
            copy.append(element.copy())

        new_matrix = copy[1:]
        for delete in new_matrix:
            del delete[i]

        y += matrix[0][i] * determinant(new_matrix) * x
        x = x * -1

    return det


def cofactor(matrix):
    """
    --Function cofactor--
    param: --> matrix
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(matrix) != len(matrix[i]) or len(matrix[i]) == 0:
            raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    new_l = []
    for o in range(len(matrix)):
        a = []
        for p in range(len(matrix)):
            copy = []
            for element in matrix:
                copy.append(element.copy())
            del copy[o]
            for delete in copy:
                del delete[p]

            if (o+p) % 2 != 0:
                x = -1
            else:
                x = 1
            a.append(determinant(copy) * x)
        new_l.append(a)
    return new_l
