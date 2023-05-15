#!/usr/bin/python3

def max_integer(my_list=[]):
    big_i = 0
    if my_list:
        for i in my_list:
            if (i < 0 and i is my_list[0]):
                big_i = i
            elif (i > big_i):
                big_i = i
        return (big_i)
    return (None)
