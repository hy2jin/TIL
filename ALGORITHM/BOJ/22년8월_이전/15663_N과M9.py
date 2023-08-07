# BOJ N과 M (9)
import sys
sys.stdin = open('input.txt')

def recur(idx):
    if idx == M:
        print(*lst)
        return
    chk = set()
    for n in range(N):
        if not u[n] and nums[n] not in chk:
            chk.add(nums[n])
            u[n] = 1
            lst[idx] = nums[n]
            recur(idx+1)
            u[n] = 0

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
u = [0] * (N+1)
lst = [0] * M

chk = set()
for n in range(N):
    if nums[n] not in chk:
        chk.add(nums[n])
        u[n] = 1
        lst[0] = nums[n]
        recur(1)
        u[n] = 0