#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print("{:2d}".format(column), end='')
        print()
