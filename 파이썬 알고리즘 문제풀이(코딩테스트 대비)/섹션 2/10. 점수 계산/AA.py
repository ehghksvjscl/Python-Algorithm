import sys

# File Path 설정
file_path = "C:/Users/dhkim/Desktop/python-algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/10. 점수 계산/in2.txt"
# sys.stdin = open(file_path, "rt")

# 값 받기
n = int(input())
arr = list(map(int, input().split()))
plus_point = 0
sum_point = 0

for i in arr:
    if i == 1:
        sum_point += (i + plus_point) 
        plus_point += 1
    else:
        plus_point = 0

print(sum_point)