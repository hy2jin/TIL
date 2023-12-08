# BOJ 2506 점수 계산
import sys
sys.stdin = open('input.txt')

N = int(input())
data = list(map(int, input().split()))

# score = [0] * N
# prev = 0
# for i in range(N):
#     if not data[i]:
#         score[i] = 0
#         prev = 0
#     elif not prev:
#         score[i] = 1
#         prev = 1
#     else:
#         score[i] = score[i-1] + 1
# print(sum(score))

score = ans = 0
for i in range(N):
    if data[i]:
        score += 1
    else:
        score = 0
    ans += score
print(ans)