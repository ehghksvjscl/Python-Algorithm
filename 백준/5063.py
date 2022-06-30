count = int(input())

for n in range(count):
    a,b,c = map(int,input().split())
    result = a - b + c

    if result > 0:
        print("do not advertise")
    elif result == 0:
        print("does not matter")
    else:
        print("advertise")

