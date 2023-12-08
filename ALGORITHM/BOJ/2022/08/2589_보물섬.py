# BOJ 2589 보물섬
import sys
sys.stdin = open('input.txt')
I = sys.stdin.readline


def BFS(i, j):
    cnt = 0
    Q = [(i, j)]
    q = 0
    while q < len(Q):
        r, c = Q[q]
        q += 1
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                if cnt < visited[nr][nc]:
                    cnt = visited[nr][nc]
                Q.append((nr, nc))
    return cnt-1        # 처음 시작 위치는 카운트하지 않음 (-1)


dr = [-1, 1, 0, 0]                      # 상 하 좌 우
dc = [0, 0, -1, 1]
N, M = map(int, I().split())
arr = [I() for _ in range(N)]           # ['WLLWWWL', 'LLLWLLL', 'LWLWLWW', 'LWLWLLL', 'WLLWLWW']

visited = [[0]*M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1
            cnt = BFS(i, j)             # 최단거리라서 BFS, 각 시작점에서의 최단거리 최대값
            if cnt > ans:               # 그 중에 최대값
                ans = cnt

print(ans)
