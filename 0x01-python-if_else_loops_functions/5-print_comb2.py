#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        print("{0:02d}".format(num))
        break
    print("{0:02d}, ".format(num), end="")
