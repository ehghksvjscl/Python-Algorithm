def factor(number):
    i = 2
    while(number!=1):
        if number%i==0:
            number = number/i
            print(i)
        else:
            i+=1



num = int(input())
factor(num)