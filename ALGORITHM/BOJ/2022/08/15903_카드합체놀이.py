# BOJ 15903 카드 합체 놀이
import sys
from heapq import heappush, heappop, heapify
sys.stdin = open('input.txt')

n, m = map(int, input().split())
Q = list(map(int, input().split()))
heapify(Q)
for _ in range(m):
    a = heappop(Q)
    b = heappop(Q)
    heappush(Q, a+b)
    heappush(Q, a+b)

print(sum(Q))
