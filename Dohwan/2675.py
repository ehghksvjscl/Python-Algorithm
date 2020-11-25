# 변수 및 입력 선언
count = int(input())
result_str = ""

# 0000 기능 : parm(000기능을 위한 값) 
def plus_string(number):
    # 0000 기능을 위한 for
    for i in range(number):
        result_str = ""
        val_list = input().split()
        val = val_list.pop(0) 
        # 문자열 조합
        for c in val_list[0]:
            for ii in range(int(val)):
                result_str += c
        # Output
        print(result_str)

plus_string(count)