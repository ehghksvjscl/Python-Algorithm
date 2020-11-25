def avg_score():
    # 변수 선언
    result_sum = 0

    for i in range(5):
        #입력
        a  = int(input())

        if a >= 40:
            result_sum += a
        else:
            result_sum += 40

    return int(result_sum / 5)

print(avg_score())