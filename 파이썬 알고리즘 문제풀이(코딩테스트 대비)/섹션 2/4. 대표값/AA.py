import sys
from itertools import *

answer = set()

# File Path 설정
file_path = "C:/Users/gusdb/Desktop/Python-Algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/4. 대표값/in1.txt"
sys.stdin = open(file_path, "rt")

# 값 받기
n = int(input())
arr = list(map(int, input().split()))

avg_arr = 0
for i in arr:
    avg_arr += i

avg_arr = round(avg_arr / len(arr))
print(avg_arr)