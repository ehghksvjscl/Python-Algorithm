import sys
import os

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

gridLength = int(input())
grid = list(map(list, [input().split() for _ in range(gridLength)]))

LeftDiagonalTotal = 0
RightDiagonalTotal = 0
result = []

for i in range(gridLength):
    horizontalTotal = 0
    verticalTotal = 0
    LeftDiagonalTotal += int(grid[i][i])
    RightDiagonalTotal += int(grid[i][gridLength - i - 1])

    for j in range(gridLength):
        horizontalTotal += int(grid[i][j])
        verticalTotal += int(grid[j][i])

    result.append(horizontalTotal)
    result.append(verticalTotal)

result.append(LeftDiagonalTotal)
result.append(RightDiagonalTotal)

print(max(result))
