#!/usr/bin/python3
num = 0
while num != 100:
    if num != 99:
        print("{:02d}".format(num), end=', ')
        num += 1
    else:
        print("{}".format(num))
        exit()
