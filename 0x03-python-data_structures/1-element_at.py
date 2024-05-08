#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    value = my_list[idx]
    if my_list[idx] < 0:
        return None
    elif my_list[idx] > length:
        return None
    else:
        return value
