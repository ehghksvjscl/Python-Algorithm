import sys

# File Path 설정
file_path = "C:/Users/gusdb/Desktop/Python-Algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/5. 정다면체/in1.txt"
# sys.stdin = open(file_path, "rt")

# 값 받기
n, m = map(int, input().split())
num_list = []
count_list = []
answer = []
result = ""

# 모든 경우의 수 List에 넣기
# for i in range(1,n+1):
#     for j in range(1, m+1):
#         num_list.append(i + j)

# # 모든 경우에 수를 Count하기 위해 중복제거
# set_number = set(num_list)

# for i in set_number:
#     count_list.append(num_list.count(i))


# for i in set_number:
#     if num_list.count(i) == max(count_list):
#         answer.append(i)

# print(" ".join(map(str, answer)))

# ----------------------------------------------------------------

# 도전
n, m = map(int, input().split())
cnt_list = [0] * ((n + m) + 1)
answer = []
sum_list = []


for i in range(1,n+1):
    for j in range(1, m+1):
        cnt_list[i+j] += 1
        sum_list.append(i+j)

max_cnt = max(cnt_list)

for i,v in enumerate(cnt_list):
    if max_cnt == v:
        answer.append(str(i))

print(" ".join(answer))

