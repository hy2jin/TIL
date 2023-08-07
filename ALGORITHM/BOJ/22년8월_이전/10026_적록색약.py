# BOJ 10026_적록색약
import sys
sys.stdin = open('input.txt')
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N = int(input())
arr = [input() for _ in range(N)]
arr2 = []
for n in range(N):
    arr2.append(arr[n].replace('R', 'G'))
visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
cnt = cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            cnt += 1
            color = arr[i][j]
            Q = [(i, j)]
            q = 0
            while q < len(Q):
                r, c = Q[q]
                q += 1
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == color and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        Q.append((nr, nc))
        if not visited2[i][j]:
            visited2[i][j] = 1
            cnt2 += 1
            color = arr2[i][j]
            Q = [(i, j)]
            q = 0
            while q < len(Q):
                r, c = Q[q]
                q += 1
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0 <= nr < N and 0 <= nc < N and arr2[nr][nc] == color and not visited2[nr][nc]:
                        visited2[nr][nc] = 1
                        Q.append((nr, nc))
print(cnt, cnt2)
