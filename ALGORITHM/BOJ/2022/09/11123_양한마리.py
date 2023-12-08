from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for _ in range(int(input())):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    cnt = 0
    for r in range(H):
        for c in range(W):
            if arr[r][c] == '#':
                cnt += 1
                arr[r][c] = '.'
                Q = deque([(r, c)])
                while Q:
                    i, j = Q.popleft()
                    for d in range(4):
                        ni, nj = i + di[d], j + dj[d]
                        if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == '#':
                            arr[ni][nj] = '.'
                            Q.append((ni, nj))
    print(cnt)
