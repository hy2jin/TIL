# BOJ 11660 구간 합 구하기 5
import sys
sys.stdin = open('input.txt')
I = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
# print(arr)
for i in range(N):
    for j in range(N):
        arr[i+1][j+1] = arr[i][j+1] + arr[i+1][j] - arr[i][j] + arr[i+1][j+1]
# print(arr)
for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    print(arr[r2][c2] - arr[r2][c1-1] - arr[r1-1][c2] + arr[r1-1][c1-1])
