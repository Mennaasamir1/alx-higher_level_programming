#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    funs = dir()
    for i in range(0, len(funs)):
        if funs[i][:2] != "__":
            print("{}".format(funs[i]))
