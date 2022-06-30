def solution(s):
    answer = ""
    str_number = ""
    new_string = []
    al = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for ch in s:
        if ch.isnumeric():
            new_string.append(ch)
        else:
            str_number += ch
            if str_number in al:
                new_string.append(str(al.index(str_number)))
                str_number = ""
            
    
    for n in new_string:
        answer += n
    
    return int(answer)