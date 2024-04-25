#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        copy_string = ""
        if i != n:
            copy_string += str[i]
        print("{}".format(copy_string))