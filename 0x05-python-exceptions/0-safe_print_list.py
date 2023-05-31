#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    a = 0
    try:
        for i in range(x):
            a += 1
            if i < (x - 1):
                print("{:d}".format(my_list[i]), end="")
            else:
                print("{:d}".format(my_list[i]))
    except IndexError:
        print("")
        a -= 1
    return (a)
