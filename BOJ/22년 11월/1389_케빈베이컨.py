'''
1. 플로이드-와샬
2. bfs
'''

N, M = map(int, input().split())

adj = [[N] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                adj[i][j] = 0
            else:
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

ans = 1
for idx in range(1, N + 1):
    if sum(adj[ans]) > sum(adj[idx]):
        ans = idx
print(ans)
