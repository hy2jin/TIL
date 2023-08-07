# BOJ 1987 알파벳
import sys
sys.stdin = open('input.txt')
I = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, I().split())
arr = [I() for _ in range(R)]
ans = 0
Q = set([(0, 0, arr[0][0])])                    # 중복 방지를 위한 set

while Q:
    r, c, path = Q.pop()
    if len(path) > ans:
        ans = len(path)
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in path:     # not in 으로 같은 알파벳 경로 제외 (이게 생각보다 오래 안걸리는듯)
            Q.add((nr, nc, path+arr[nr][nc]))   # 지나온 경로 가지고 다니기

print(ans)
