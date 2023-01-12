import sys
import os
from functools import reduce

filePath = "{}/in2.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

count = int(input())
inbody = []

for d in range(count):
    inbody.append(list(map(int, input().split())))
inbody.sort(key=lambda x: (x[0], x[1]), reverse=True)

w = inbody[0][1]
cnt = 1

for i in range(1, count):
    if inbody[i][1] > w:
        cnt+=1
        w = inbody[i][1]

print(cnt)