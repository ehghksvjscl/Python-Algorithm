import sys
import os
from functools import reduce

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

s, n = input().split()
n = int(n)
stack = []

for x in s:
    while n > 0 and stack and stack[-1] < int(x):
        stack.pop()
        n -= 1

    stack.append(int(x))

if n != 0:
    stack = stack[:-n]

print(reduce(lambda x, y: str(x) + str(y), stack))
