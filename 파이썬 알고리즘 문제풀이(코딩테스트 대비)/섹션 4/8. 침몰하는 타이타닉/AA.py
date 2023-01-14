import sys
import os
from collections import deque

filePath = "{}/in3.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
cnt = 0

# while l:
#     if l[0] + l[-1] <= m and len(l) > 1:
#         cnt += 1
#         l.pop(0)
#         l.pop(-1)
#     else:
#         cnt += 1
#         l.pop(0)

# print(cnt)

# deque
l = deque(l)
while l:
    if l[0] + l[-1] <= m and len(l) > 1:
        cnt += 1
        l.popleft()
        l.pop()
    else:
        cnt += 1
        l.pop()

print(cnt)
