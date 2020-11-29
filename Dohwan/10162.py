num = int(input())
a = 0
b = 0
c = 0

if num // 300 >= 1:
    a = num // 300
    num = num % 300

if num // 60 >= 1:
    b = num // 60 
    num = num % 60

if num // 10 >= 1:
    c = num // 10

if num % 10 != 0:
    print("-1")
else:
    print(a,b,c)