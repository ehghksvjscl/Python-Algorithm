import sys
import os

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")
_, findNumber = map(int, input().split())
numberList = list(map(int, input().split()))
numberList.sort()

lt = 0
rt = len(numberList) - 1
mid = 0

for i in range(len(numberList)):
    mid = (lt + rt) // 2
    if numberList[mid] == findNumber:
        break
    elif numberList[mid] < findNumber:
        lt = mid
    else:
        rt = mid - 1
    
print(mid+1)
