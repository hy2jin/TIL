# BOJ 15900 나무 탈출
'''
루트노드에서 각 리프까지 depth의 합이
짝수이면 선공이 지고, 홀수이면 선공이 이긴다
'''
import sys
sys.setrecursionlimit(30000)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def DFS(v, depth):
    global res
    child = len(adj[v])

    for nv in adj[v]:
        if visited[nv]:         # 방문한적 있음 -> 리프노드가 아님
            child -= 1          # 리프노드가 아님 -> 자식의 수 - 1
        else:
            visited[nv] = 1
            DFS(nv, depth+1)

    if child == 0:              # 자식의 수가 0 -> 리프노드
        res += depth


N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)
res = 0
visited = [0] * (N+1)
visited[1] = 1
DFS(1, 0)
print('Yes') if res%2 else print('No')


### 다른풀이 ########################################################


def DFS(v):
    for nv in adj[v]:
        if visited[nv] == -1:               # 방문한적 없으면
            visited[nv] = visited[v] + 1    # 자식 깊이 = 부모깊이 + 1
            DFS(nv)


N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

visited = [-1] * (N+1)      # value: 루트에서의 깊이
visited[1] = 0              # 루트노드의 깊이: 0
DFS(1)

res = 0
for i in range(2, N+1):
    if len(adj[i]) == 1:    # 리프노드일때
        res += visited[i]   # 깊이
print('Yes') if res%2 else print('No')
