import sys
import os

filePath = "{}/in1.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
gridLength = int(input())
grid = [list(map(int, input().split())) for _ in range(gridLength)]
grid.insert(0, [0]*gridLength)
grid.append([0]*gridLength)
for x in grid:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, gridLength + 1):
    for j in range(1, gridLength +1):
        if all(grid[i][j] > grid[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)


# newGrid = [[0 for _ in range(gridLength)] for _ in range(gridLength)]

# for y in range(gridLength):
#     for x in range(gridLength):
#         if x == 0:
#             if grid[y][x] <= grid[y][x + 1]:
#                 continue
#             else:
#                 newGrid[y][x] +=1
#         elif x == gridLength - 1:
#             if grid[y][x] <= grid[y][x - 1]:
#                 continue
#             else:
#                 newGrid[y][x] +=1
#         else:
#             if grid[y][x] <= grid[y][x + 1] or grid[y][x] <= grid[y][x - 1]:
#                 continue
#             else:
#                 newGrid[y][x] +=1

# for y in range(gridLength):
#     for x in range(gridLength):
#         if newGrid[y][x] == 0:
#             continue

#         if y == 0:
#             if grid[y][x] <= grid[y + 1][x]:
#                 newGrid[y][x] -= 1
#             else:
#                 continue
#         elif y == gridLength - 1:
#             if grid[y][x] <= grid[y - 1][x]:
#                 newGrid[y][x] -= 1
#             else:
#                 continue
#         else:
#             if grid[y][x] <= grid[y + 1][x] or grid[y][x] <= grid[y - 1][x]:
#                 newGrid[y][x] -= 1
#             else:
#                 continue

# print(*grid, sep='\n')
# print(*newGrid, sep='\n')

# print(sum(map(sum, newGrid)))
