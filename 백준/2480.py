# 변수 선언 및 입력 받기
dice_number = input().split()


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

print(getmoney(dice_number))