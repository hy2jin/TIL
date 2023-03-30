# BOJ 15650 N과 M (4)
import sys
sys.stdin = open('input.txt')

def recur(num, idx):
    if idx == M:
        print(*lst)
        return
    for n in range(num, N+1):
        lst[idx] = n
        recur(n, idx+1)

N, M = map(int, input().split())
lst = [0] * M
for n in range(1, N+1):
    lst[0] = n
    recur(n, 1)