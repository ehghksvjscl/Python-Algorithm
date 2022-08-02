import sys

# File Path 설정
file_path = "C:/Users/dhkim/Desktop/python-algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/4. 대표값/in2.txt"
# sys.stdin = open(file_path, "rt")

# 값 받기
max_value = 0
result_index = 0
n = int(input())
min_value = 9999999
arr = list(map(int, input().split()))
answer = []

# round는 논리적 문제가 있음
# avg_arr = round(sum(arr) / len(arr))

# 평균값 구하기
avg_arr = sum(arr) / len(arr)
avg_arr += 0.5
avg_arr = int(avg_arr)


# 평균값과 가까운 값 구하기
for i in arr:
    if min_value > abs(avg_arr - i):
        min_value = abs(avg_arr - i)

# 가까운 값과 같은 값을 담기
for k,v in enumerate(arr):
    if min_value ==  abs(avg_arr - v):
        answer.append((k,v))

# 같은 갑 중 우선순위가 높은 값과 인덱스 추출(값이 큰가, 값이 크다면 인덱스가 큰가)
for i in answer:
    if max_value < i[1]:
        max_value = i[1]
        result_index = i[0]

# 답지의 소스코드
min_value = 9999999

for i,v in enumerate(arr):
    temp = abs(v-avg_arr)
    if temp<min_value:
        min_value = temp
        socre = v
        res=i+1
    elif temp==min_value:
        if v > socre:
            socre = v
            res=i+1

# print(avg_arr, result_index+1)
print(avg_arr, res)