#!/usr/bin/python3
from sys import argv
if __name__ != "__main__":
    exit
argc = len(argv) - 1
if (argc == 0):
    print("0 arguments.")
elif (argc == 1):
    print("{0} argument:\n{0}: {1}".format(argc, argv[1]))
else:
    print("{} arguments:".format(argc))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
