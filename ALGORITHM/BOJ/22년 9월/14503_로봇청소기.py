N, M = map(int, input().split())
# d : 0=북, 1:동, 2:남, 3:서
r, c, d = map(int, input().split())
# 0:빈칸, 1:벽
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
arr[r][c] = 2
turn = 0
while True:
    d = (d+3)%4
    turn += 1
    nr, nc = r + dr[d], c + dc[d]
    if arr[nr][nc] == 0:
        arr[nr][nc] = 2
        ans += 1
        r, c = nr, nc
        turn = 0
    elif turn == 4:
        nd = (d+2)%4
        nr, nc = r + dr[nd], c + dc[nd]
        if arr[nr][nc] != 1:
            r, c = nr, nc
            turn = 0
        else:
            break
print(ans)
