def check(x, y, a, b, dots):
    i = (dots[x][0] - dots[y][0]) * (dots[a][1] - dots[b][1])
    j = (dots[a][0] - dots[b][0]) * (dots[x][1] - dots[y][1])
    return i == j

def solution(dots):
    if check(0, 1, 2, 3, dots):
        return 1
    if check(0, 2, 1, 3, dots):
        return 1
    if check(0, 3, 1, 2, dots):
        return 1
    return 0
