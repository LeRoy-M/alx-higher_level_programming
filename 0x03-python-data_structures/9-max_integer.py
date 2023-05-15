#!/usr/bin/python3

def max_integer(my_list=[]):
    big_i = 0
    if my_list:
        for int(i) in my_list:
            if i > big_i:
                big_i = i
        return (big_i)
    return (None)
