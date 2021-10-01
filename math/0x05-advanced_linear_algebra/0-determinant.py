#!/usr/bin/env python3
""" task 0 """


def rows(x, row, matrix):
    """
    ---Def rows
    param: ---> X,row,matrix
    """
    list = []
    for r in row:
        A = []
        for c in range(len(matrix)):
            if c != x:
                A.append(r[c])
        list.append(A)
    return list


def determinant(matrix):
    """
    --Function determ--
    param:
    --> matrix
    """
    if matrix == [[]]:
        return 1
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    if len(matrix[0]) != len(matrix):
        raise ValueError("matrix must be a square matrix")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a list of lists")
        elif len(i) != len(matrix):
            raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        a = (matrix[1][1] * matrix[0][0]) - (matrix[1][0] * matrix[0][1])
        return a
    determ = 0
    for i, j in enumerate(matrix[0]):
        row = [rw for rw in matrix[1:]]
        mini_mat = []
        mini_mat = rows(i, row, matrix)

        determ = determ + (j * (-1) ** i * determinant(mini_mat))

    return determ
