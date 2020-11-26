# 변수 선언 및 입력 받기
get_input = int(input())
sum_list = []


def getmoney(dice):
    result = 0

    for i in dice:
        if dice.count(i) == 2:
            result = 0
            result = int(i) * 100 + 1000
            break

        if dice.count(i) == 3:
            result = 0        
            result = int(i) * 1000 + 10000
            break

        if dice.count(i) == 1:
            result = int(max(dice_number)) * 100

    return result

for i in range(get_input):
    dice_number = input().split()
    sum_list.append(getmoney(dice_number))

print(max(sum_list))