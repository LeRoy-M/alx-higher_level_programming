#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for i in range(x):
        try:
            a += 1
            if (my_list[i]):
                print("{:d}".format(my_list[i]), end="")
            if i == (x - 1):
                print("")
        except (ValueError, TypeError):
            if i == (x - 1):
                print("")
            a -= 1

    return (a)
