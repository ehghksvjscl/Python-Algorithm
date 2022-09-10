import sys

# File Path 설정
file_path = "C:/Users/dhkim/Desktop/python-algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/2. 숫자만 추출/in1.txt"
# sys.stdin = open(file_path, "rt")

# 값 받기
s = input()
number_string = ""
count = 0

for c in s:
    if ord("0") <= ord(c) and ord("9") >= ord(c):
        number_string += c

num_val = int(number_string)

for i in range(num_val//2):
    if num_val % (i+1) == 0:
        count += 1
        

print(int(number_string))
print(count+1)