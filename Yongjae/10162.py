T_list = []
def Microwave(T):
    while T > 0 and T <= 10000 and T != 0:
        if T >= 300:
            T_list.append(300)
            T = T - 300
        if T >= 60 and T < 300:
            T_list.append(60)
            T = T - 60
        if T > 0 and T < 60:
            T_list.append(10)
            T = T - 10

T = int(input())
Microwave(T)
A = T_list.count(300)
B = T_list.count(60)
C = T_list.count(10)
if T % 10 != 0 or T == 0:
    print(-1)
else:
    print(A, B, C)