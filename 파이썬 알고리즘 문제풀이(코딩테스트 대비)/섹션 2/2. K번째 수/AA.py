import sys

answer = 0

# File Path 설정
# file_path = "C:/Users/gusdb/Desktop/Python-Algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/2. K번째 수/in2.txt"
# sys.stdin = open(file_path, "rt")

# 1. Test case 만큼 for문을 돌린다.
T = int(input())
for i in range(T):
    # 2. N(글자수), s(start_point), e(end_point), k(추출 Index)를 선언한다.
    _,s,e,k=map(int, input().split())
    arr = list(map(int, input().split()))
    # 3. s,e 지점까지 글자수를 자른다.
    start_index = s-1
    end_index = e
    output_index = k -1

    new_arr = sorted(arr[start_index:end_index]) 
    # 4. 자른 글자의 k번째 글자를 구해 출력을 한다.

    answer = (new_arr[output_index])

    print(f"#{i+1} {answer}")