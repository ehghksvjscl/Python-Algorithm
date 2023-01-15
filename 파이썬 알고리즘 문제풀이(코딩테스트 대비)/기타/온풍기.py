office = [[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 1, 0]]
# office = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
k = 2 - 1
cntList = []

for i in range(len(office)):
    for j in range(len(office)):
        cnt = 0

        up = 0
        down = 0
        left = 0
        right = 0

        if office[i][j] == 1:
            # 위로 더 가능
            if i - k >= 0:
                up = 1

            # 아래로 더 가능
            if i + k < len(office):
                down = 1

            # 왼쪽으로 더 가능
            if j - k >= 0:
                left = 1

            # 오른쪽으로 더 가능
            if j + k < len(office):
                right = 1

        if up == 1:
            if left == 1:
                for y in range(i, i - k - 1, -1):
                    for x in range(j - k, j + 1):
                        if office[y][x] == 1:
                            cnt += 1

                cntList.append(cnt)
                cnt = 0

            if right == 1:
                for y in range(i, i - k - 1, -1):
                    for x in range(j, j + k + 1):
                        if office[y][x] == 1:
                            cnt += 1

                cntList.append(cnt)
                cnt = 0

        if down == 1:
            if left == 1:
                for y in range(i, i + k + 1):
                    for x in range(j - k, j + 1):
                        if office[y][x] == 1:
                            cnt += 1

                cntList.append(cnt)
                cnt = 0

            if right == 1:
                for y in range(i, i + k + 1):
                    for x in range(j, j + k + 1):
                        if office[y][x] == 1:
                            cnt += 1

                cntList.append(cnt)
                cnt = 0

print(max(cntList))
