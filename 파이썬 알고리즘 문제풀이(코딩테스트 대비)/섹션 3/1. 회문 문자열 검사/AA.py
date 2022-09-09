import sys

# File Path 설정
file_path = "C:/Users/dhkim/Desktop/python-algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/1. 회문 문자열 검사/in1.txt"
# sys.stdin = open(file_path, "rt")

# 값 받기
n = int(input())

for i in range(n):
    input_value = input().upper()
    toggle = True
    for j in range(len(input_value) // 2):
        if input_value[j] != input_value[-1-j]:
            toggle = False

    if toggle:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")