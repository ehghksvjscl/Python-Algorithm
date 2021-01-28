N = int(input())
j = 0
OX = []
OX_sum = 0
point = 0
for i in range(N):
    OX = list(input())
    OX_sum = 0
    point = 0
    for j in range(len(OX)):
        if OX[j] == 'O':
            point += 1
            OX_sum = OX_sum + point
        elif OX[j] == 'X':
            point = 0
    print(OX_sum)