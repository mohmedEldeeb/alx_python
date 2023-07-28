#!/usr/bin/python3
import sys

def printArges():
    count_args = len(argv)
    argv = sys.argv[1:]
    print("{}".format(count_args), end="")
    if count_args == 0:
        print(" arguments.", end="\n")
    elif count_args == 1:
        print(" argument:\n1: {}".format(argv[0]), end="\n")
    else:
        print(" arguments:", end="\n")

        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    printArges()