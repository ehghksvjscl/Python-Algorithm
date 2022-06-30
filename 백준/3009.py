# 변수 선언 및 입력
first_dot = input().split()
secend_dot = input().split()
three_dot = input().split()

x_dot = [first_dot[0] ,secend_dot[0] , three_dot[0]]
y_dot = [first_dot[1] , secend_dot[1] , three_dot[1]]


def select_dot_point(odd_dot,even_dot):
    x = 0; y = 0
    
    for i,odd in enumerate(odd_dot):
        if odd_dot.count(odd) == 1:
            x = int(odd)
            break

    for i,even in enumerate(even_dot):
        if even_dot.count(even) == 1:
            y = int(even)
            break

    print(x,y)

select_dot_point(x_dot,y_dot)