office = [[5, -1, 4], [6, 3, -1], [2, -1, 1]]
r = 1
c = 0
move = ["go", "go", "right", "go", "right", "go", "left", "go"]


def solution(office, r, c, move):
    북 = (-1, 0)
    동 = (0, 1)
    남 = (1, 0)
    서 = (0, -1)

    현방향 = 북
    현위치 = (r, c)

    먼지 = office[r][c]
    office[r][c] = 0

    for m in move:
        if m == "go":
            if 현위치[0] + 현방향[0] < 0 or 현위치[1] + 현방향[1] < 0:
                continue

            if 현위치[0] + 현방향[0] > len(office) - 1 or 현위치[1] + 현방향[1] > len(office) - 1:
                continue

            if office[현위치[0] + 현방향[0]][현위치[1] + 현방향[1]] == -1:
                continue

            현위치 = (현위치[0] + 현방향[0], 현위치[1] + 현방향[1])

            먼지 += office[현위치[0]][현위치[1]]
            office[현위치[0]][현위치[1]] = 0

        elif m == "right":
            if 현방향 == 북:
                현방향 = 동
            elif 현방향 == 동:
                현방향 = 남
            elif 현방향 == 남:
                현방향 = 서
            elif 현방향 == 서:
                현방향 = 북
        elif m == "left":
            if 현방향 == 북:
                현방향 = 서
            elif 현방향 == 동:
                현방향 = 북
            elif 현방향 == 남:
                현방향 = 동
            elif 현방향 == 서:
                현방향 = 남

    return 먼지
