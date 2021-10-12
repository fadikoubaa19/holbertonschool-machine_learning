#!/usr/bin/env python3
"""function that cal the matrix of matrix"""


def determinant(matrix):
    """
    Function determinant:
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
    for i in range(len(matrix)):
        copy = []
        for elements in matrix:
            copy.append(elements.copy())

        new_matrix = copy[1:]
        for delete in new_matrix:
            del delete[a]

        y += matrix[0][i] * determinant(new_matrix) * x
        x = x * -1

    return y


def cofactor(matrix):
    """
    Function cofactor
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

    new_matrix = []
    for a in range(len(matrix)):
        aux = []
        for b in range(len(matrix)):
            copy = []
            for ele in matrix:
                copy.append(ele.copy())
            del copy[a]
            for delete in copy:
                del delete[b]

            if (a+b) % 2 != 0:
                y = -1
            else:
                y = 1
            aux.append(determinant(copy) * y)
        new_matrix.append(aux)
    return new_matrix


def adjugate(matrix):
    """
    Function adjugate:
    param: --> matrix
    """
    coffar = cofactor(matrix)
    adjacente = []

    for i in range(len(matrix)):
        copy = []
        for j in range(len(matrix)):
            copy.append(coffar[j][i])
        adjacente.append(copy)

    return adjacente
