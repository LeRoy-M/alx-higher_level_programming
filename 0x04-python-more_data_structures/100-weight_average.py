#!/usr/bin/python3

def weight_average(my_list=[]):
    scre, wght = 0, 0
    if not my_list:
        return (None)

    for t in my_list:
        scre += t[0] * t[1]
        wght += t[1]

    return (scre / wght)
