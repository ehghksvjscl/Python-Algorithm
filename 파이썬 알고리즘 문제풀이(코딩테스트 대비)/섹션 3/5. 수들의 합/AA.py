import sys
import os

filePath = "{}/in3.txt".format(os.path.dirname(os.path.abspath(__file__)))

if sys.argv[-1] == "local":
    sys.stdin = open(filePath, "rt")

listLength, ListSumValue  = list(map(int, input().split()))
numberList = list(map(int, input().split()))
lt = 0
rt = 1
tot = numberList[0]
cnt = 0

while True:
    if tot<ListSumValue:
        if rt<listLength:
            tot += numberList[rt]
            rt += 1
        else:
            break
    elif tot == ListSumValue:
        cnt += 1
        tot -= numberList[lt]
        lt += 1
    else:
        tot -= numberList[lt]
        lt += 1

print(cnt)
        

# 접근 방식이 좀 그러다. 
# 왜 슬라이스로 풀려고 했냐?
# 반성하자

# for i in range(listLength):
#     for j in range(i,listLength):
#         sumValue = sum(numberList[i:j])
#         if  sumValue == ListSumValue:
#             print(numberList[i:j])
#             result += 1

#         if sum(numberList[i:j]) > ListSumValue:
#             break

# print(result)