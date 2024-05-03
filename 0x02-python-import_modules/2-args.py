#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    i = 0

    if length < 1:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, sys.argv[1]))
    else:
        print("{} arguments:".format(length))
        for i in range(length):
            i += 1
            print("{}: {}".format(i, sys.argv[i]))
