import sys
import os
from functools import reduce

filePath = "{}/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/3. 카드 역배치/in1.txt".format(os.getcwd())
# sys.stdin = open(filePath, "rt")

cardList = [i for i in range(1, 21)]

for i in range(10):
    parms = list(map(int, input().split()))
    startPoint = parms[0]-1
    endPoint = parms[1]

    reverseList = (list(reversed(cardList[startPoint:endPoint])))
    result = cardList[:startPoint] + reverseList + cardList[endPoint:]

    cardList = result

print(reduce(lambda total, x: str(total) + " " + str(x), result))