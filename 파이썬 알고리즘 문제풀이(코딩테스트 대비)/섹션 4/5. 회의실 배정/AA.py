import sys
import os
from functools import reduce

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

count = int(input())
meetingTimes = []

for d in range(count):
    meetingTimes.append(list(map(int, input().split())))
meetingTimes.sort(key=lambda x: (x[1], x[0]))

endTime = meetingTimes[0][1]
cnt = 1

for i in range(1, count):
    startTime = meetingTimes[i][0]

    if startTime >= endTime:
        endTime = meetingTimes[i][1]
        cnt += 1
    
print(cnt)
