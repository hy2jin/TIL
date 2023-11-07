from collections import deque

direc = [( -1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(i, j):
    points = [(i, j)]
    sub = A[i][j]
    vi[i][j] = 1
    Q = deque([(i, j)])
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr, nc = r + direc[d][0], c + direc[d][1]
            if isConnected(r, c, nr, nc):
                points.append((nr, nc))
                sub += A[nr][nc]
                vi[nr][nc] = 1
                Q.append((nr, nc))
    cnt = len(points)
    for point in points:
        A[point[0]][point[1]] = sub//cnt

def move(r, c):
    dir_return = 0
    for d in range(4):
        nr, nc = r + direc[d][0], c + direc[d][1]
        if isConnected(r, c, nr, nc):
            dir_return += 1
    return dir_return > 0  

def isConnected(r, c, nr, nc):
    if 0 <= nr < N and 0 <= nc < N:
        if vi[nr][nc]: return False
        diff = abs(A[nr][nc] - A[r][c])
        if diff < L or diff > R: return False
        return True
    return False

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    vi = [[0] * N for _ in range(N)]
    flag = True
    for r in range(N):
        for c in range(N):
            if vi[r][c]: continue
            if move(r, c):
                BFS(r, c)
                flag = False
    if flag: break
    else: ans += 1
print(ans)
