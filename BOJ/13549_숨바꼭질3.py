# BOJ 13549 숨바꼭질 3
from heapq import heappush, heappop

INF = int(1e20)
N, K = map(int, input().split())

if K <= N:
    print(N - K)
    exit()

visited = [INF] * 200001
Q = []
heappush(Q, (0, N))
visited[N] = 0

while Q:
    t, v = heappop(Q)
    for nt, nv in ((t+1, v-1), (t+1, v+1), (t, v*2)):
        if 0 <= nv < 200001 and nt < visited[nv]:
            visited[nv] = nt
            heappush(Q, (nt, nv))

print(visited[K])
