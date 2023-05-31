#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    a = 0
    try:
        for i in range(x):
            a += 1
            if (my_list[i]):
                print("{:d}".format(my_list[i]), end="")
        print("")
    except IndexError:
        print("")
        a -= 1
    return (a)
