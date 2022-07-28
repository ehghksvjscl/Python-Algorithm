import sys
from itertools import *

answer = set()

# File Path 설정
file_path = "C:/Users/gusdb/Desktop/Python-Algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/3. k번째 큰 수/in1.txt"
# sys.stdin = open(file_path, "rt")

# 값 받기
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 모든 경우의 수
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            answer.add(arr[i] + arr[j] + arr[m])

# 정렬
answer = list(answer)
answer = sorted(answer, reverse=True)

print(answer[k-1])