num = int(input()) #구하고싶은 숫자 입력
i = 1
def Greatest(i):
    while i * (i + 1) / 2 <= num: #최소공배수 조건문
        i += 1 #1씩 증가
    return i-1 #호출 함수 리턴값

print(Greatest(i)) #함수 호출