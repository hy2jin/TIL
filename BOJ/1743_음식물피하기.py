import sys
sys.stdin = open('input.txt')
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M, K = map(int, input().split())
arr = [[0]*(M) for _ in range(N)]
rc = []
for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1
    rc.append((i-1, j-1))
visited = [[0]*M for _ in range(N)]
ans = 1
for r, c in rc:
    if not visited[r][c]:
        q = [(r, c)]
        visited[r][c] = 1
        cnt = 0
        while q:
            n, m = q.pop(0)
            cnt += 1
            for d in range(4):
                nn, nm = n+dr[d], m+dc[d]
                if 0 <= nn < N and 0 <= nm < M and arr[nn][nm] and not visited[nn][nm]:
                    visited[nn][nm] = 1
                    q.append((nn, nm))
        ans = max(ans, cnt)
print(ans)