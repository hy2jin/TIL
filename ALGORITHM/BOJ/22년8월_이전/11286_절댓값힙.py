# BOJ 11286 절댓값 힙
import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
Q = []
for _ in range(N):
    n = int(input())
    if n > 0:
        heappush(Q, [n, n])
    elif n < 0:
        heappush(Q, [-n, n])
    elif Q:
        print(heappop(Q)[1])
    else:
        print(0)
