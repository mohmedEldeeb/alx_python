#!/usr/bin/python3
from 0-add import add
if __name__ == "__main__":
  a = 1
  b = 2
  result = add(a, b)
  print("{:d} + {:d} = {:d}".format(a, b, result),end="\n")
