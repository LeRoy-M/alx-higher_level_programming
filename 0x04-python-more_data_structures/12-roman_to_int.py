#!/usr/bin/python3

def roman_to_int(roman_string):
    I, V, X, L, C, D, M, num = 1, 5, 10, 50, 100, 500, 1_000, 0
    if (roman_string is None or not isinstance(roman_string, str)):
        return (0)
    for rch in roman_string:
        if rch == "M":
            num += M
        elif rch == "D":
            num += D
        elif rch == "C":
            num += C
        elif rch == "L":
            num += L
        elif rch == "X":
            num += X
        elif rch == "V":
            num += V
        elif rch == "I":
            if rch is roman_string[-1]:
                num += I
            else:
                num -= I
        else:
            continue
    return (num)
