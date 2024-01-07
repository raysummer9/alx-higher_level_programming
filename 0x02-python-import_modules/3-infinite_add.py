#!/usr/bin/python3
import sys


x = sys.argv[1:]
result = sum(int(arg) for arg in x)
print(result)


