# BOJ 2564 경비원
w, h = map(int, input().split())
N = int(input())
store = [list(map(int, input().split())) for _ in range(N)]
dir, d = map(int, input().split())
dis = 0
for s in store:
    if dir == s[0]:
        dis += abs(d - s[1])
        continue
    tmp = d + s[1]
    if dir == 1:
        if s[0] == 2:
            tmp = tmp + h if tmp < w + w - tmp else w + w - tmp + h
        elif s[0] == 4:
            tmp = w - d + s[1]
    elif dir == 2:
        if s[0] == 1:
            tmp = tmp + h if tmp < w + w - tmp else w + w - tmp + h
        elif s[0] == 3:
            tmp = h + d - s[1]
        else:
            tmp = h + w - tmp
    elif dir == 3:
        if s[0] == 2:
            tmp = h - d + s[1]
        elif s[0] == 4:
            tmp = tmp + w if tmp < h + h - tmp else h + h - tmp + w
    elif dir == 4:
        if s[0] == 1:
            tmp = d + w - s[1]
        elif s[0] == 2:
            tmp = h + 2 - tmp
        else:
            tmp = tmp + w if tmp < h + h - tmp else h + h - tmp + w
    dis += tmp
print(dis)