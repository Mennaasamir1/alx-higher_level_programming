#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value is int:
            return True
    except TypeError:
        return False
