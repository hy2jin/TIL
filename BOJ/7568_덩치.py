# BOJ 7568 덩치
import sys
sys.stdin = open('input.txt')

N = int(input())
ans = []
data= [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    x, y = data[i]
    cnt = 0
    for j in range(N):
        if i == j: continue
        p, q = data[j]
        if x < p and y < q: cnt += 1
    ans.append(cnt+1)

print(*ans)
