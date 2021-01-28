chang = 100
sang = 100
i = 0
N = int(input())
for i in range(N):
    chang_point, sang_point = map(int, input().split())
    if chang_point > sang_point:
        sang = sang - chang_point
    if chang_point < sang_point:
        chang = chang - sang_point
    if chang_point == sang_point:
        None

print(chang, sang)