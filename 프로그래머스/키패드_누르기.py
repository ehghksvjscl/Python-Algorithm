def pos(left, right, num, hand):
    keypad = {
        "1":(0,0), "2":(0,1), "3":(0,2),
        "4":(1,0), "5":(1,1), "6":(1,2),
        "7":(2,0), "8":(2,1), "9":(2,2),
        "*":(3,0), "0":(3,1), "#":(3,2)
    }
    abs_left = abs(keypad[num][0] - keypad[left][0]) + abs(keypad[num][1] - keypad[left][1])
    abs_right = abs(keypad[num][0] - keypad[right][0]) + abs(keypad[num][1] - keypad[right][1])
    
    # print(num)
    # print(abs_left)
    # print(abs_right)
    # print("______________________")
    
    if abs_left > abs_right:
        return "R"
    elif abs_left < abs_right:
        return "L"
    else:
        if hand == "right":
            return "R"
        else:
            return "L"


def solution(numbers, hand):
    answer = ''
    left = "*"
    right = "#"
    
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left = str(num)
        elif num in [3,6,9]:
            answer += 'R'
            right = str(num)
        else:
            result = pos(left, right, str(num), hand)
            answer += result
            
            if result == "R":
                right = str(num)
            else:
                left = str(num)
    
    return answer