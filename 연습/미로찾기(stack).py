"""
1. 상하좌우 이동하는 리스트를 만들어 준다.
2. 벽인지 아닌지 Check하는 함수를 만들어 준다.
3. 2를 찾는 로직을 톨려 x,y를 채워 준다.
4. 스택에 시작 위치를 넣어 준다.
5. 스택이 빌때까지 반복한다.
6. 스택에 있는 값을 꺼내 현제 위치에 1을 넣어 준다.
7. 이동할 4가지 방향을 Check한다.
8. 가는 길이 벽이면 Continue를 한다.
9. 가는 길이 3이면 결과를 저장 한 후 Break를 한다.
10. 9번이 아닌 경우 값이 O이므로 스택에 추가해 준다.
11. for-else 구문으로 countinue와 break를 명시한다.
"""
# 0 변수 선언
result = 0
x,y = 0,0
N = 5
map_list = [[1,3,1,0,1],
            [1,0,1,0,1],
            [1,0,1,0,1],
            [1,0,1,0,1],
            [1,0,0,2,1],
]

# 1
move_list = [(0,1), (0,-1), (1,0), (-1,0)]

# 2
def is_well(x,y):
    if x<0 or y<0 or y>=N or x>=N:
        return True
    
    return False

# 3
for i in range(N):
    if 2 in map_list[i]:
        x = map_list[i].index(2)
        y = i
        break

# 4
stack = [(y,x)]

# 5
while(stack):
    # 6
    y,x = stack.pop()
    map_list[y][x] = 1

    # 7
    for _y, _x in move_list:
        dy = _y + y
        dx = _x + x

        # 8
        if is_well(dy, dx):
            continue


        # 9
        if map_list[dy][dx] == 3:
            result += 1
            break

        # 10
        elif map_list[dy][dx] == 0:
            stack.append([dy,dx])
            print(stack)
    else:
        continue

    break

print(result)
