num = int(input())

def change(s):
    point = 0
    result = 0
    for c in s:
        if c == "O":
            point += 1
            result += point
        else:
            point = 0
            result += point

    return result



for n in range(num):
    string = input()
    print(change(string))
    