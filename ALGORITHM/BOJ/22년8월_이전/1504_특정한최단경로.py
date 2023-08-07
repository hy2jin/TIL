# BOJ 1504 특정한 최단 경로
import sys
from heapq import heappush, heappop
# input = sys.stdin.readline
sys.stdin = open('input.txt')


def dijkstra(s):
    Q = []
    heappush(Q, [0, s])
    dis = [INF] * (N + 1)
    dis[s] = 0
    while Q:
        w, v = heappop(Q)
        for nw, nv in adj[v]:
            if w + nw < dis[nv]:
                dis[nv] = w + nw
                heappush(Q, [w + nw, nv])
    return dis


N, E = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append([c, b])       # a에서 b로 가는 거리 c
    adj[b].append([c, a])       # b에서 a로 가는 거리 c
v1, v2 = map(int, input().split())

INF = int(1e9)
dis_1 = dijkstra(1)             # 1에서 시작하는 최단거리
dis_v1 = dijkstra(v1)           # v1에서 시작하는 최단거리
dis_v2 = dijkstra(v2)           # v2에서 시작하는 최단거리

ans1 = dis_1[v1] + dis_v1[v2] + dis_v2[N]       # 1 -> v1 -> v2 -> N
ans2 = dis_1[v2] + dis_v2[v1] + dis_v1[N]       # 1 -> v2 -> v1 -> N
ans = min(ans1, ans2)
if ans >= INF:
    ans = -1
print(ans)
