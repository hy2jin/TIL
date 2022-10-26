# BOJ N과 M (12)
import sys
sys.stdin = open('input.txt')

def recur(idx, si):
    if idx == M:
        print(*lst)
        return
    chk = set()
    for n in range(si, N):
        if nums[n] not in chk:
            chk.add(nums[n])
            lst[idx] = nums[n]
            recur(idx+1, n)

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
lst = [0] * M

chk = set()
for n in range(N):
    if nums[n] not in chk:
        chk.add(nums[n])
        lst[0] = nums[n]
        recur(1, n)
