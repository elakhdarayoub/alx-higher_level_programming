#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = []
    for item in a_dictionary:
        if a_dictionary[item] == value:
            keys.append(item)
    if len(keys) > 0:
        for key in keys:
            del a_dictionary[key]
    return a_dictionary
