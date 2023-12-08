from heapq import heappush, heappop

def solution(N, road, K):
    adj = [[] for _ in range(N + 1)]
    for a, b, c in road:
        adj[a].append((c, b))
        adj[b].append((c, a))

    hq = []
    heappush(hq, (0, 1))
    time = [float('inf')] * (N + 1)
    time[1] = 0
    
    while hq:
        t, v = heappop(hq)
        for dt, nv in adj[v]:
            nt = dt + t
            if nt < time[nv]:
                time[nv] = nt
                heappush(hq, (nt, nv))
    
    return len([t for t in time if t <= K])