# BOJ 11724 연결 요소의 개수
import sys
sys.stdin = open('input.txt')


def DFS(v):
    for w in adj[v]:
        if not V[w]:
            V[w] = 1
            DFS(w)


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
V = [0] * (N+1)
cnt = 0
for i in range(1, N+1):
    if not V[i]:
        cnt += 1
        V[i] = 1
        DFS(i)
print(cnt)
