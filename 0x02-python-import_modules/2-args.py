#!/usr/bin/python3
if __name__ == "__main__":
<<<<<<< HEAD
    from sys import argv
    count = len(argv) - 1
=======
    import sys
    count = len(sys.argv) - 1
    i = 0
>>>>>>> 407309f3efdd1e4c942dcd3868ea72bb3fbb6d77
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
<<<<<<< HEAD
        print("{}: {}".format(i + 1, argv[i + 1]))
=======
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
>>>>>>> 407309f3efdd1e4c942dcd3868ea72bb3fbb6d77
