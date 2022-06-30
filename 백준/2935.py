def change_str(string,num1,num2):
    if string == "*":
        return num1 * num2
    else:
        return num1 + num2

first_num = int(input())
char = input()
secend_num = int(input())

print(change_str(char,first_num,secend_num))