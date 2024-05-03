#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    i = 0

    if length < 1:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))
    for i in range(length):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
