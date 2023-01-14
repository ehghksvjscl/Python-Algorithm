import sys
import os
from functools import reduce

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

n = int(input())
array = list(map(int, input().split()))

tmp = [0] * n

for i in range(n):
    for j in range(n):
        if array[i] == 0 and tmp[j] == 0:
            tmp[j] = i + 1
            break
        elif tmp[j] == 0:
            array[i] -= 1

print(*tmp)
#
