num = int(input())
string_arr = input()

sort_arr = sorted(string_arr)
# print(sort_arr)

first_person = sort_arr.count(sort_arr[0])
secend_person = sort_arr.count(sort_arr[-1])

if first_person > secend_person:
    print(sort_arr[0])
elif first_person < secend_person:
    print(sort_arr[-1])
elif first_person == secend_person:
    print("Tie")