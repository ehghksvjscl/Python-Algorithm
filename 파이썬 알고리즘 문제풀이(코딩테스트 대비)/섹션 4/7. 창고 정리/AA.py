import sys
import os
from functools import reduce

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

l = int(input())
boxs = list(map(int, input().split()))
boxs.sort(reverse=True)
m = int(input())

for i in range(m):
    boxs[0] -= 1
    boxs[-1] += 1

    if boxs[0] < boxs[1] or boxs[-1] > boxs[-2]:
        boxs.sort(reverse=True)

print(boxs[0] - boxs[-1])
