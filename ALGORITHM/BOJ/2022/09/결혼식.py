n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
ans = set(adj[1])
for i in adj[1]:
    for j in adj[i]:
        if j > 1: ans.add(j)
print(len(ans))