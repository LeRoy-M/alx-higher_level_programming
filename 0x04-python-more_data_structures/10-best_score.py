#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None: return None
    key = ""
    keys = list(a_dictionary.keys())
    for i in range(len(keys)):
        if i == len(keys) - 1:
            break
        if (a_dictionary[keys[i]] > a_dictionary[keys[i + 1]]):
            key = keys[i]
        else:
            key = keys[i + 1]

    return (key)
