#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_one = {}
    for key, val in a_dictionary.items():
        if val != value:
            new_one[key] = val
    a_dictionary.clear()
    a_dictionary.update(new_one)
    return a_dictionary
