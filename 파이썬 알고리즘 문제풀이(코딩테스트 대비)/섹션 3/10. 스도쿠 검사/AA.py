import sys
import os

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

grid = [list(map(int, input().split())) for _ in range(9)]

def check(grid):
    for i in range(9):
        hCheckList = [0] * 10
        vCheckList = [0] * 10
        for j in range(9):
            hCheckList[grid[i][j]] = 1
            vCheckList[grid[j][i]] = 1

        if sum(hCheckList) != 9 or sum(vCheckList) != 9:
            return "NO"

    for i in range(3):
        for j in range(3):
            gCheckList = [0] * 10
            for k in range(3):
                for s in range(3):
                    gCheckList[grid[i*3+k][j*3+s]] = 1
            
            if sum(gCheckList) != 9:
                return "NO"

    return "YES"

print(check(grid))