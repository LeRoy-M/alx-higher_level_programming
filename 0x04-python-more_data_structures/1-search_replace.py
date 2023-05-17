#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    list(map(lambda i: new_list.append(replace) if (
        search == i) else new_list.append(i), my_list))

    return (new_list)
