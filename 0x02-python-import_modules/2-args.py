#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    i = 0
    if count == 0:
        print("{} argument.".format(count))
    elif count == 1:
        print("{} arguments:".format(count))
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
