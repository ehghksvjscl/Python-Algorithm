def solution(new_id):
    answer = ''
    
    first_string = ''
    second_string = ''
    three_string = ''
    fore_string = ''
    five_string = ''
    
    dot_continue = 0
    
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    
    for ch in new_id:
        # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
        if ch.isalpha():
            first_string += ch
        elif ch.isdigit():
            first_string += ch
        elif ch in ['-','_','.']:
            first_string += ch
    
    # print("first", first_string)
    
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    for ch in first_string:
        if ch == '.':
            dot_continue +=1
            if not dot_continue >= 2:
                second_string += ch

        else:
            second_string += ch
            dot_continue = 0

    # print("second", second_string)
            
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if len(second_string) == 1 and second_string[0] == '.':
        three_string = ""
    elif second_string[0] == '.':
        three_string = second_string[1:]
        if second_string[-1] == '.':
            three_string = three_string[:-1]
    elif second_string[-1] == '.':
        three_string = second_string[:-1]
    else:
        three_string = second_string
        
    # print("three", three_string)
    
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(three_string) == 0:
        fore_string = "a"
    else:
        fore_string = three_string
        
    # print("fore", fore_string)

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(fore_string) >= 16:
        five_string = fore_string[0:15]
        if five_string[-1] == '.':
            five_string = five_string[0:-1]
    else:
        five_string = fore_string
    
    # print("five", five_string)
    
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    answer = five_string
    
    if len(answer) <= 2:
        while(len(answer) <= 2):
            answer += answer[-1]
            
    # print("final", answer)
    
    return answer