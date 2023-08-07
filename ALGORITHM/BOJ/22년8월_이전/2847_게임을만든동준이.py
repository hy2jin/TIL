# BOJ 2847 게임을 만든 동준이
import sys
sys.stdin = open('input.txt')

N = int(input())
score = [int(input()) for _ in range(N)]
ans = 0
for i in range(N-2, -1, -1):
    if score[i] >= score[i+1]:
        minus = score[i] - score[i+1] + 1
        score[i] -= minus
        ans += minus
print(ans)