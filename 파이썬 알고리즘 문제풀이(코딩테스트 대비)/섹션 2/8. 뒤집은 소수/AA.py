import sys

# File Path 설정
file_path = "C:/Users/ehghk/Desktop/python-algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/8. 뒤집은 소수/in3.txt"
# sys.stdin = open(file_path, "rt")

# 값 받기
n = int(input())
arr = list(map(int, input().split()))
answer = []


def reverse(x):
    string_number = str(x)
    list_str_number = []

    for i in string_number:
        list_str_number.append(i)

    list_str_number.reverse()

    result = "".join(list_str_number)
    return int(result)


def isPrime(x):
    if x == 1:
        return False

    for i in range(2, int(x/2)):
        if x % i == 0:
            return False

    return True


for i in arr:
    reverse_value = reverse(i)
    if isPrime(reverse_value):
        answer.append(str(reverse_value))

print(" ".join(answer))
