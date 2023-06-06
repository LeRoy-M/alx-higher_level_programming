#!/usr/bin/python3
from sys import argv
"""Program to solve the N queens problem"""


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    if isinstance(int(argv[1]), int):
        n = int(argv[1])
        if (n < 4):
            print("N must be at least 4")
            exit(1)
except ValueError:
    print("N must be a number")
    exit(1)

class NQueens:
    """Class to solve the N queens problem"""
    def __init__(self, n):
         """Initialization method"""
         self.__n = n

    #def __str__(self):
         """Initialization method"""
         #pass #return

    def  solve_n_queens(self):
        """Method to solve N queens problem"""
        col = set()
        pos_diag = set() # r + c
        neg_diag = set() # r - c
        result = []
        board = [["0"] * self.__n for i in range(self.__n)]

        def backtrack(r):
            """Backtracking method"""
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "1"

                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "0"

        backtrack(0)
        return (result)

solution = NQueens(n)
print(solution.solve_n_queens())
