#!/usr/bin/python3
"""This module contains a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    new_mat = [[] for i in range(2)]
    """Function for matrix division"""
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if not isinstance(matrix[x][y], int) and
            not isinstance(matrix[x][y], float):
                raise TypeError("matrix must be a matrix
                                (list of lists) of integers/floats")
            new_mat[x].append(round(matrix[x][y] / div, 2))
    return new_mat
