# BOJ 1051 숫자 정사각형
import sys
sys.stdin = open('input.txt')
ans = 1
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)
for r in range(N):
    for c in range(M-1):
        for cc in range(c+1, M):
            rr = r + cc - c
            if rr < N and arr[r][c] == arr[r][cc] and arr[r][c] == arr[rr][c] and arr[r][cc] == arr[rr][cc]:
                area = (cc - c + 1)**2
                ans = max(ans, area)
print(ans)