#!/usr/bin/python3

def roman_to_int(roman_string):
    I, V, X, L, C, D, M, num = 1, 5, 10, 50, 100, 500, 1_000, 0
    if (roman_string is None or not isinstance(roman_string, str)):
        return (0)
    for rn in roman_string:
        if rn == "M":
            num += M
        elif rn == "D":
            num += D
        elif rn == "C":
            num += C
        elif rn == "L":
            num += L
        elif rn == "X":
            num += X
        elif rn == "V":
            num += V
        elif rn == "I":
            num += I
        else:
            continue
    return (num)
