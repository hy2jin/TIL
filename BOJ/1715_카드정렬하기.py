# BOJ 1715 카드 정렬하기
import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')

Q = []
for _ in range(int(input())):
    heappush(Q, int(input()))
ans = 0
while len(Q) > 1:
    tmp = heappop(Q) + heappop(Q)
    ans += tmp
    heappush(Q, tmp)
print(ans)
