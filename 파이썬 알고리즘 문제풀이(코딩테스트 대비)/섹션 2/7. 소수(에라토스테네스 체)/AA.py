import sys

# File Path 설정
file_path = "C:/Users/gusdb/Desktop/Python-Algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/7. 소수(에라토스테네스 체)/in2.txt"
# sys.stdin = open(file_path, "rt")

# 값 받기
n = int(input())

# n개만큼 배열 받기
n_list = [0]*(n+1)

# 소수 구하기
cnt = 0
for i in range(2, n+1):
    if n_list[i] == 0:
        cnt += 1
        for j in range(i, n+1, i): # 효율성 있게..
            n_list[j] = 1

# 출력
print(cnt)