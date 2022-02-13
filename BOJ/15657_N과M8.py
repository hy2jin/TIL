# BOJ N과 M (8)
import sys
sys.stdin = open('input.txt')

def recur(idx, si):
    if idx == M:
        print(*lst)
        return
    for n in range(si, N):
        lst[idx] = nums[n]
        recur(idx+1, n)

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
lst = [0] * M
for n in range(N):
    lst[0] = nums[n]
    recur(1, n)
