# BOJ 1976 여행 가자
import sys
from collections import deque
sys.stdin = open('input.txt')
'''
N: 도시의 수
M: 여행 계획에 속한 도시의 수
adj: (i행 j열) i도시에서 j도시의 연결 정보, 연결됨: 1, 연결되지 않음: 0
plan: 여행 계획
'''

N = int(input())
M = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x: int(x)-1, input().split()))

ans = 'YES'
for i in range(M-1):
    TF = False
    s, e = plan[i], plan[i+1]
    Q = deque([s])
    visited = [0] * N
    visited[s] = 1
    while Q:
        v = Q.popleft()
        if v == e:          # s에서 e로 갈 수 있음
            TF = True
            break
        for j in range(N):
            if adj[v][j] and not visited[j]:
                visited[j] = 1
                Q.append(j)
    if not TF:              # s에서 e로 갈 수 없음
        ans = 'NO'
        break
print(ans)