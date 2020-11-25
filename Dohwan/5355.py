def change_value(num,string):
    if string=='@':
        return (num*3)
    elif string=="%":
        return (num+5)
    elif string=="#":
        return (num-7)

a = int(input())
for i in range(a):
    str_list = input().split()
    value = float(str_list.pop(0))
    for c in str_list:
        value = change_value(value,c)

    print("%.2f" % value)