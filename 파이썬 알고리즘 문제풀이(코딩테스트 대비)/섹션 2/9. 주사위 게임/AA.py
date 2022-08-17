import sys

# 규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
# 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
# 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다. 

# File Path 설정
file_path = "C:/Users/gusdb/Desktop/Python-Algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/9. 주사위 게임/in4.txt"
# sys.stdin = open(file_path, "rt")

# 값 받기
n = int(input())
prize_money_list = []

for i in range(n):
    dices = list(map(int, input().split()))
    dice1, dice2, dice3 = dices[0], dices[1], dices[2]

    if dice1 == dice2 == dice3:
        prize_money_list.append(10000 + (dice1 * 1000))
    elif dice1 == dice2 or dice1 == dice3:
        prize_money_list.append(1000 + (dice1 * 100))
    elif dice2 == dice3:
        prize_money_list.append(1000 + (dice2 * 100))
    else:
        prize_money_list.append(max(dices) * 100) 

print(max(prize_money_list))
