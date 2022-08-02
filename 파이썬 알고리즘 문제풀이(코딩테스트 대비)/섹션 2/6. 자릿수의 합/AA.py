import sys

# File Path 설정
file_path = "C:/Users/gusdb/Desktop/Python-Algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/6. 자릿수의 합/in2.txt"
# sys.stdin = open(file_path, "rt")

# 값 받기
n = int(input())
arr = list(map(str, input().split()))
max_value = 0
result_value = 0

def digit_sum(x: str):
    _sum = 0
    for num in x:
        _sum += int(num)

    return([x,_sum])

for x in arr:
    result = digit_sum(x)
    if result[1] > max_value:
        max_value = result[1]
        result_value = result[0]

print(result_value)
