import sys
import os
from functools import reduce

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

firstListLength = input()
firstList = list(map(int, input().split()))
secondListLength = input()
secondList = list(map(int, input().split()))

result = firstList + secondList
print(reduce(lambda t,x: str(t) + " " + str(x),sorted(result)))