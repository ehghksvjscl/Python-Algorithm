# 해당 문제는 문제 채점 프로그램용 입니다.
import sys
N,K=map(int, input().split())
# N = 25
# K = 5
answer = []

for i in range(1,N+1):
    if N % i == 0:
        answer.append(i)

if K > len(answer) or len(answer) == 0:
    print(-1)
else:
    print(answer[K-1])