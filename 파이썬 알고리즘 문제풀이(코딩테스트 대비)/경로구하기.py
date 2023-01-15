r = 2
c = 4

grid = [[0] * c] * r


def CountWay(endPoint):
    if endPoint == startPoint:
        return 1
    else:
        x, y = endPoint
        if x == 0:
            return CountWay((x, y - 1))
        elif y == 0:
            return CountWay((x - 1, y))
        else:
            return CountWay((x - 1, y)) + CountWay((x, y - 1))


startPoint = (0, 0)
endPoint = (r - 1, c - 1)
way = CountWay(endPoint)

print(way)
