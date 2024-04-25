#!/usr/bin/python3
def remove_char_at(str, n):
copy_string = ""
for i in range(len(str)):
    if i != n:
        copy_string = str[i]
return (copy_string)