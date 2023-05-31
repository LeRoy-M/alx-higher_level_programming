#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for i in range(x):
        try:
            a += 1
            if (my_list[i]):
                print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            a -= 1
    print("")

    return (a)
