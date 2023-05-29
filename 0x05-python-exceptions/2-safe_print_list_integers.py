#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    a = 0
    if my_list:
        for i in range(x):
            a += 1
            try:
                try:
                    print("{:d}".format(my_list[i]), end="")
                    if i == (x - 1):
                        print("")
                except (ValueError, TypeError):
                    if i == (x - 1):
                        print("")
                    a -= 1
                    continue
            except IndexError:
                print("")
                a -= 1
                break
    return (a)
