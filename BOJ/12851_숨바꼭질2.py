# BOJ 12851 숨바꼭질2
from collections import deque

N, K = map(int, input().split())
if K <= N:
    print(f'{N-K}\n1')
    exit()


def q_append(preidx, idx):
    if 0 <= idx < 200001:
        if visited[idx] == -1 or visited[idx] >= visited[preidx] + 1:
            visited[idx] = visited[preidx] + 1
            q.append(idx)
            return 1


def check(idx):
    if idx == K:
        return 1
    return 0


visited = [-1] * 200001         # visited[N]값은 N에 도달하는데 걸린 시간
q = deque()
q.append(N)
visited[N] = 0
cnt = 0
while q:
    X = q.popleft()
    if q_append(X, X-1):
        cnt += check(X-1)
    if q_append(X, X+1):
        cnt += check(X+1)
    if q_append(X, X*2):
        cnt += check(X*2)

print(f'{visited[K]}\n{cnt}')
