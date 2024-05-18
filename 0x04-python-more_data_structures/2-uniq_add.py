#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    set1 = set(my_list)
    new_list = list(set1)
    for i in new_list:
        sum += i
    return sum
