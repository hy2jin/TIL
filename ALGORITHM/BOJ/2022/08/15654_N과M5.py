# BOJ N과 M (5)
import sys
sys.stdin = open('input.txt')

def recur(idx):
    if idx == M:
        print(*lst)
        return
    for n in range(N):
        if u[n] == 0:
            lst[idx] = nums[n]
            u[n] = 1
            recur(idx+1)
            u[n] = 0

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
lst = [0] * M
u = [0] * (N+1)

for n in range(N):
    lst[0] = nums[n]
    u[n] = 1
    recur(1)
    u[n] = 0
