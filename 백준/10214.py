T = int(input())

for _ in range(T):
    Y = K = 0

    for _ in range(9):
        a,b = map(int,input().split())
        Y += a
        K += b

    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")