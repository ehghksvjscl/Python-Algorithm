count_num = int(input())

# 두수의 최소공약수
def gcd(num1,num2):
    while(num2!=0):
        r = num1%num2
        num1 = num2
        num2 = r

    return num1

# 두수의 최대 공배수
def lcm(num1,num2):
    return int(num1*num2 / gcd(num1,num2))

for i in range(count_num):
    first_num,sec_num = map(int,input().split())
    print(lcm(first_num,sec_num))
