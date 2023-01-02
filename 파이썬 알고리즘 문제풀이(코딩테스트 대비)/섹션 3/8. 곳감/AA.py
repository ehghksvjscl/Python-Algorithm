import sys
import os
from functools import reduce

filePath = "{}/in3.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

gridLength = int(input())
grid = [list(map(int, input().split())) for _ in range(gridLength)]

LEFT = 0
RIGHT = 1

changeCycle = int(input())
for _ in range(changeCycle):
    row, direction, changeCount = map(int, input().split())
    changeCount %= gridLength
    newGrid = [0 for _ in range(gridLength)]
    for i in range(gridLength):
        if direction == LEFT:
            newGrid[i - changeCount] = grid[row - 1][i]
        else:
            newGrid[(i + changeCount) % gridLength] = grid[row - 1][i]

    grid[row - 1] = newGrid


startPoint = 0
endPoint = gridLength
result = 0
for i in range(gridLength):
    if i < gridLength // 2:
        result += sum(grid[i][startPoint:endPoint])
        startPoint += 1
        endPoint -= 1
    else:
        result += sum(grid[i][startPoint:endPoint])
        startPoint -= 1
        endPoint += 1

print(result)
