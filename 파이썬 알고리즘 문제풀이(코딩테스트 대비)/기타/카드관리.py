보유돈 = 0
거래횟수 = 6
거래내역 = [('d', 10), ('r', 20), ('p', 5), ('d', 10),('d', 10), ('r', 6)]
거래내역2 = [('d', 10), ('p', 5), ('r', 5), ('r', 5),('p', 10), ('d', 10)]
r_list = []

for i in 거래내역2:
    if i[0] == 'd':
        보유돈 += i[1]
    elif i[0] == 'r':
        if 보유돈 >= i[1]:
            보유돈 -= i[1]
        else:
            r_list.append(i[1])

    elif i[0] == 'p':
        if 보유돈 >= i[1]:
            보유돈 -= i[1]

    r_list = list(set(r_list))

    if r_list:
        if 보유돈 >= r_list[0]:
            보유돈 -= r_list[0]
        

print(보유돈)