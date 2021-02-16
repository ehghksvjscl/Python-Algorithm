# 배열의 크기 N
# 숫자가 더해지는 수 M
# 한 숫자가 더하는 수 K

# 5,8,3
# 2 4 5 4 6  =  46

import time

N,M,K = map(int,input().split())
num_array = [int(x) for x in input().split()]
result_num = 0
plus_count = 0

start_time = time.time() 

num_array.sort()

first_num = num_array.pop()
second_num = num_array.pop()

for i in range(M):
    if plus_count < K:
        plus_count += 1
        result_num += first_num
    else:
        plus_count = 0
        result_num += second_num

end_time = time.time()
print("시간 측정 : ",end_time-start_time)

print(result_num)