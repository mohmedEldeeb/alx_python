#!/usr/bin/python3
import sys

def printArges():
    count_args = len(argv)
    argv = sys.argv[1:]
    if count_args == 0:
        print(count_args, "arguments.",end="\n")
    elif count_args == 1:
        print(count_args, "argument:",end="\n")
    else:
        print(num_argue, "arguments:",end="\n")

        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    printArges()