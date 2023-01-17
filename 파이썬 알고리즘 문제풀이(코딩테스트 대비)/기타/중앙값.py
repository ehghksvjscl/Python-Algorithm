n = 5
a = [1,5,3,-1,3]
r = []

for i in range(1, n+1):
    mi = len(a[:i]) // 2
    sort_list = sorted(a[:i])

    if mi == 0:
        r.append(sort_list[mi])

    elif len(sort_list) % 2 == 0:
        print(sort_list, mi)
        if sort_list[mi-1] < sort_list[mi]:
            r.append(sort_list[mi -1])
        else:
            r.append(sort_list[mi])
    else:

        r.append(sort_list[mi])


print(" ".join(map(str, r)))