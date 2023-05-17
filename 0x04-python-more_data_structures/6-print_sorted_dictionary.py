#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    #for i in (sorted(a_dictionary.items(), key = lambda k: k[0])):
    for i in (sorted(a_dictionary.items())):
        print(i)
