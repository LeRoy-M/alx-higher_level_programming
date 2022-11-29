#!/usr/bin/python3
"""
    This module solves the N queens problem
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(sys.argv[1])
except:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

print("Module Name: {}".format(sys.argv[0]))
print("Value of N: {}".format(N))
print("Argv Count: {}".format(len(sys.argv)))
