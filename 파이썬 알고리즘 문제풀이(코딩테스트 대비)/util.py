# 모든 경우의 수
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            answer.add(arr[i] + arr[j] + arr[m])