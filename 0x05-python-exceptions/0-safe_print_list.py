#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    if my_list:
        for i in range(x):
            try:
                if i < (x - 1):
                    print("{:d}".format(my_list[i]), end="")
                else:
                    print("{:d}".format(my_list[i]))
            except IndexError:
                print("")
                i -= 1
                break
    return (i+1)
