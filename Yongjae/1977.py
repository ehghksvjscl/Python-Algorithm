M = int(input())
N = int(input())
i = 1
Squared_list = []
while N <= 10000 and M <= N and M <= 10000:
    Squared = i * i
    if M <= Squared <= N:
        Squared_list.append(Squared)
    if N < Squared:
        break
    i += 1

if sum(Squared_list) > 0:
    print(sum(Squared_list))
    print(min(Squared_list))
else:
    print(-1)