N = int(input())
i = 1
if 1<=N<=9:
    for i in range(1, 10):
        dex = N * i
        print(f'{N}', '*', i, '=', dex)
