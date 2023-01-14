import sys
import os
from functools import reduce

filePath = "{}/in3.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
cnt = 0

while len(l) > 0:
    if l[0] + l[-1] <= m and len(l) > 1:
        cnt += 1
        l.pop(0)
        l.pop(-1)
    else:
        cnt += 1
        l.pop(0)

print(cnt)
