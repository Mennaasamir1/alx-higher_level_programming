#!/usr/bin/python3
def remove_char_at(str, n):
    copy_string = ""
    i = 0
    for char in str:
        if i != n:
            copy_string += str[i]
        i += 1
    return (copy_string)
