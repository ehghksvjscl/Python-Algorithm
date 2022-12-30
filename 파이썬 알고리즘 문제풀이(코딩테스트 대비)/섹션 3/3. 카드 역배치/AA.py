import sys
import os
from functools import reduce

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

cardList = [i for i in range(1, 21)]

for i in range(10):
    parms = list(map(int, input().split()))
    startPoint = parms[0]-1
    endPoint = parms[1]

    reverseList = (list(reversed(cardList[startPoint:endPoint])))
    result = cardList[:startPoint] + reverseList + cardList[endPoint:]

    cardList = result

print(reduce(lambda total, x: str(total) + " " + str(x), result))