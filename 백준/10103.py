num = int(input())

person1 = 100
person2 = 100

for i in range(num):
    a,b = map(int,input().split())
    
    if a > b:
        person2 = person2 - a
    elif a < b:
        person1 = person1 - b
    
print(person1)
print(person2)