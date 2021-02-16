import time

# N,M,K 공백으로 구분하여 입력 받기
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

start_time = time.time() 

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

end_time = time.time()
print("시간 측정 : ",end_time-start_time)

print(result) # 최종 답안 출력