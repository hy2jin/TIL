# BOJ 8979 올림픽
'''
list -> key, lambda 사용하여 정렬하기
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
nations = [[] for _ in range(N)]
for i in range(N):
    nations[i] = list(map(int, input().split()))
nations.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
for j in range(N):
    if nations[j][0] == K:
        break
    if nations[j][1:] != nations[j+1][1:]:
        rank = j + 2
print(rank)
