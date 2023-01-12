import sys
import os
from functools import reduce

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

distince, hours = map(int, input().split())
pointList = []
for d in range(distince):
    pointList.append(int(input()))
pointList.sort()

def Count(mid):
    cnt = 1
    ep = pointList[0]
    for i in range(1, distince):
        if pointList[i] - ep >= mid:
            cnt += 1
            ep = pointList[i]

    return cnt

lt = 1
rt = pointList[-1]
res = 0

while lt<=rt:
    mid = (rt + lt) // 2
    if Count(mid) >= hours:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)