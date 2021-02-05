from random import randint
import time

def randint_input(count):
    array = []
    for _ in range(count):
        array.append(randint(1,100)) # 1부터 100까지 정수 랜덤으로 넣기
    return array
    
# 배열에 count개의 정수 입력
array = randint_input(10000)

# 선택 정렬 시간 복잡도 계산
start_time = time.time() 

# 선택 정렬 코드
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i],array[min_index] = array[min_index],array[i] # 스위칭

# 측정 종료 및 출력
end_time = time.time()
print("선택 정렬 시간 측정 : ",end_time-start_time)

# 배열에 count개의 정수 입력(초기화)
array = randint_input(10000)

# 기본 정렬 라이브러리 시간 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

# 측정 종료 및 출력
end_time = time.time()
print("선택 정렬 시간 측정 : ",end_time-start_time)