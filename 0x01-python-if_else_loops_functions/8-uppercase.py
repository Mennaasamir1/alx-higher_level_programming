#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ltr = i
        if ord(ltr) >= 97 and ord(ltr) <= 122:
            ltr = chr(ord(i) - 32)
        print("{}".format(ltr), end='')
   print()
