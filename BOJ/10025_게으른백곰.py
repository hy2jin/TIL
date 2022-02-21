# BOJ 10025 게으른 백곰
import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

tmp = []
L = 0
for _ in range(N):
    tmp.append(list(map(int, input().split())))
    if tmp[-1][1] > L: L = tmp[-1][1]

ice = [0] * (L+1)
for g, x in tmp: ice[x] = g

right = 2*K + 1
now = sum(ice[:right])
ans = now

for i in range(right, L):
    now += (ice[i] - ice[i-right])
    ans = max(now, ans)
print(ans)