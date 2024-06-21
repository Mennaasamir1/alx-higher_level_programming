#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_of_vals = 0
    division = 0
    for i in my_list:
        sum_of_vals += i[0] * i[1]
        division += i[-1]
    return sum_of_vals/division
