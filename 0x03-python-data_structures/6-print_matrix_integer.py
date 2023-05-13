#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j is i[-1]:
                print("{}".format(j))
                continue
            print("{}".format(j), end=" ")
