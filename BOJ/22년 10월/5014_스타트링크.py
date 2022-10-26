from collections import deque

F, S, G, U, D = map(int, input().split())
ans = INF = 9876543210

Q = deque([(S, 0)])
vis = [INF] * (F + 1)
vis[S] = 0

while Q:
    now, cnt = Q.popleft()
    d, u = now - D, now + U

    if d > 0 and vis[d] > cnt + 1:
        vis[d] = cnt + 1
        Q.append((d, cnt + 1))

    if u <= F and vis[u] > cnt + 1:
        vis[u] = cnt + 1
        Q.append((u, cnt + 1))

print(vis[G]) if vis[G] < INF else print("use the stairs")
