def gcd(a,b):
    
    big = 0
    smail = 0
    remains = 0
    
    if a > b:
        big = a
        smail = b
    else:
        big = b
        smail = a
        
    while(smail != 0):
        remains = big % smail
        big = smail
        smail = remains
            
    return big

def lcm(a,b):
    return a * b / gcd(a,b)

def solution(arr):
    answer = arr[0]
    for i,v in enumerate(arr):
        if i == 0:
            pass
        else:
            answer = lcm(answer, arr[i])
    return answer