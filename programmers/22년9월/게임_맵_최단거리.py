from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    # (거리, 행, 열)
    Q = deque([(1, 0, 0)])
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    while Q:
        d, r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == 1:
                maps[nr][nc] = d+1
                Q.append((d+1, nr, nc))
    return maps[N-1][M-1] if maps[N-1][M-1] > 1 else -1