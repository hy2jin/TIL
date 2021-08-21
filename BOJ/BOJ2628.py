# BOJ 2628 종이자르기

import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
N = int(input())
cutting = [[], []]      # 0:가로로 자르는 점선(높이), 1:세로로 자르는 점선(너비)
for _ in range(N):
    tmp, n = map(int, input().split())
    cutting[tmp].append(n)

cutting[0] = sorted(cutting[0]) + [h]
cutting[1] = sorted(cutting[1]) + [w]
# 세로, 가로 최대 길이 찾기
max_h, max_w = cutting[0][0], cutting[1][0]
for i in range(1, len(cutting[0])):
    if max_h < cutting[0][i] - cutting[0][i-1]:
        max_h = cutting[0][i] - cutting[0][i-1]
for j in range(1, len(cutting[1])):
    if max_w < cutting[1][j] - cutting[1][j-1]:
        max_w = cutting[1][j] - cutting[1][j-1]
print(max_w * max_h)