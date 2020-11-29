s1,s2,s3,s4,axis = 0,0,0,0,0
c = int(input())

for i in range(c):
    a,b = map(int,input().split())

    if a > 0 and b > 0:
        s1 +=1
    elif a < 0 and b < 0:
        s3 +=1
    elif a > 0 and b < 0:
        s4 +=1
    elif a < 0 and b > 0:
        s2 +=1
    elif a == 0 or b == 0:
        axis +=1

print(f"Q1: {s1}")
print(f"Q2: {s2}")
print(f"Q3: {s3}")
print(f"Q4: {s4}")
print(f"AXIS: {axis}")
        
