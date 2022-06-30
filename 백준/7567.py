dish_input  =input()
hight = 0

for i,c in enumerate(dish_input):
    if i == 0:
        hight += 10
    else:
        if dish_input[i-1] == dish_input[i]:
            hight += 5
        else:
            hight += 10

print(hight)
