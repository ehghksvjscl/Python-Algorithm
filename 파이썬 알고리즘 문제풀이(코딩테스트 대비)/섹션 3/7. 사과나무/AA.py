import sys
import os
from functools import reduce

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

gridLength = int(input())
grid = [list(map(int, input().split())) for _ in range(gridLength)]
half = gridLength // 2
result = 0

for i in range(gridLength):
    if i <= half:
        result += reduce(lambda total, x: total + x, grid[i][half-i: half+i+1], 0)
    else:
        result += reduce(lambda total, x: total + x, grid[i][i-half: gridLength-(i-half)], 0)

print(result)