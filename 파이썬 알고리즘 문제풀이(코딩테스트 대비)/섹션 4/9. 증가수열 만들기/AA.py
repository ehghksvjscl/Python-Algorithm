import sys
import os
from collections import deque

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

n = int(input())
array = list(map(int, input().split()))
res = ""
last = 0
lt = 0
rt = n - 1
tmp = []

while lt <= rt:
    if array[lt] > last:
        tmp.append((array[lt], "L"))

    if array[rt] > last:
        tmp.append((array[rt], "R"))

    tmp.sort()

    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == "L":
            lt += 1
        else:
            rt -= 1

    tmp.clear()

print(len(res))
print(res)
