import sys
import os
from functools import reduce

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

singCount, hasDVD = map(int, input().split())
recordTimeList = list(map(int, input().split()))

lt = 1
rt = sum(recordTimeList)
res = 0
maxx = max(recordTimeList)

while lt<=rt:
    mid = (rt + lt) // 2 
    cnt = 1
    total = 0
    for i in recordTimeList:
        if total + i > mid:
            cnt += 1
            total = 0
        
        total += i

    if mid>= maxx and cnt <= hasDVD:
        rt = mid - 1
        res = mid
    else:
        lt = mid + 1

print(res)