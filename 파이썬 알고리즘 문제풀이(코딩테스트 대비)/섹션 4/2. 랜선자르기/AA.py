import sys
import os
from functools import reduce

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

listCnt, maxLanCable = map(int, input().split())
lanCableList = list(int(input()) for _ in range(listCnt))

def totalCnt(len):
    cnt = reduce(lambda t,x: t+(x//len), lanCableList, 0)
    return cnt

lt = 1
rt = max(lanCableList)
res = 0

while lt<=rt:
    mid = (rt + lt) // 2
    if totalCnt(mid) >= maxLanCable:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)


