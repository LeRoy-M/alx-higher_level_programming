#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    new_list = 0
    try:
        for i in range(x):
            if int(my_list[i]):
                new_list += 1
                print("{:d}".format(my_list[i]), end="")
            else:
                continue
        print()
    except (TypeError, ValueError):
        print()
    
    return new_list
