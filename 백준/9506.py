def 약수(num):
    result_list = []
    for i in range(1,num-1):
        if num % i == 0:
            result_list.append(i)

    return result_list


while(True):
    num = int(input())
    if num == -1:
        break

    result = 약수(num)
    p_string = f"{num} = "

    if num == sum(result):
        for n in result:
            if result[-1] == n:
                p_string += f"{n}"
            else:
                p_string += f"{n} + "

        print(p_string)
    else:
        print(f"{num} is NOT perfect.")


