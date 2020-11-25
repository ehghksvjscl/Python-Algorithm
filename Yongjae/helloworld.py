num = int(input())
i = 2
def factorization(i,num):
    while num!=1:
        if num%i == 0:
            num = num/i
            print(i)
        else:
            i += 1
factorization(i,num)