# 입력 받기
input_val = int(input())


# 수들의 합 function
def number_is_sum(num):
    # 변수 선언
    sum_val = 0
    start_val = 0

    while(sum_val+start_val < num):
        start_val += 1
        sum_val += start_val 

    return start_val

print(number_is_sum(input_val))
