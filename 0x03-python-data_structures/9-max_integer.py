#!/usr/bin/python3
def max_integer(my_list=[]):
     if my_list:
        sorting = sorted(my_list, reverse=True)
        return sorting[0]
     else:
        return (None)
