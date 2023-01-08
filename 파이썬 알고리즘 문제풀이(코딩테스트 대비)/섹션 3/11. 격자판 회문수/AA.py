import sys
import os

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

grid = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

# 가로를 구했고
for i in range(7):
    for j in range(3):
        if grid[i][j : j + 5] == list(reversed(grid[i][j : j + 5])):
            cnt += 1

# 세로를 구했다.
for k in range(7):
    for j in range(3):
        chList = []
        for i in range(5):
            chList.append(grid[i + j][k])

        if chList == list(reversed(chList)):
            cnt += 1


print(cnt)
