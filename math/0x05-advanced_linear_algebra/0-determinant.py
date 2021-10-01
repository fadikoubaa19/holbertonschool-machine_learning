#!/usr/bin/env python3
"""file ==> function determinant(matrix) """


def determinant(matrix):
    """
    matrix : List of lists
    list[[]] represent a 0x0 matrix
    return the determiannt of matrix
    """

    # if matrix is not list of lists raise type error included with msg
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")

    # if matrix isn"t a square raise type error includded with msg
    if matrix == [[]]:
        return 1
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a list of lists")

        # if length matrix diff of legnth[i] type raise error included with msg
        if len(matrix) != len(matrix[i]):
            raise ValueError("matrix must be a square matrix")

    # if length of matrix == 1 return matrix
    if len(matrix) == 1:
        return matrix[0][0]
    # if length of matrix == 2 retrun matrix 0
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    mult = 1
    deter = 0
    for i in range(len(matrix)):
        copy = []
        for ele in matrix:
            copy.append(ele.copy())

        # return determ of matrix
        new_matrix = copy[1:]
        for delete in new_matrix:
            del delete[i]

        deter += matrix[0][i] * determinant(new_matrix) * deter
        mult = mult * -1

    return deter
