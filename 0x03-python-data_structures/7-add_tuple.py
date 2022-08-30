#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    temp1, temp2 = [0, 0], [0, 0]

    if len(tuple_a) == 2:
        tuple_a2 = tuple_a
    elif len(tuple_a) == 1:
        for i in range(len(tuple_a)):
            if tuple_a[i]:
                temp1[i] = tuple_a[i]
            else:
                temp1[i] = 0
        tuple_a2 = (temp1[0], temp1[1])
    elif len(tuple_a) == 0:
        tuple_a2 = (temp1[0], temp1[1])
    
    if len(tuple_b) == 2:
        tuple_b2 = tuple_b
    elif len(tuple_b) == 1:
        for i in range(len(tuple_b)):
            if tuple_b[i]:
                temp2[i] = tuple_b[i]
            else:
                temp2[i] = 0
        tuple_b2 = (temp2[0], temp2[1])
    elif len(tuple_b) == 0:
        tuple_b2 = (temp2[0], temp2[1])
    
    new_tuple = ((tuple_a2[0] + tuple_b2[0]), (tuple_a2[1] + tuple_b2[1]))

    return new_tuple
