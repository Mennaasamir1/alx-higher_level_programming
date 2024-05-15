#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        sort_out = sorted(my_list, reverse=True)
        return sort_out[0]
    else:
        return None
