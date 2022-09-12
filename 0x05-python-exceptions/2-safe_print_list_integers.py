#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    new_list = 0
    for i in range(x):
        try:
            if int(my_list[i]):
                new_list += 1
                print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            pass
    print()

    return new_list
