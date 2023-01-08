import sys
import os

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

grid = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(3):
    for j in range(7):
        temp = grid[j][i : i + 5]
        if temp == temp[::-1]:
            cnt += 1

        for k in range(2):
            if grid[i + k][j] != grid[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1

print(cnt)
