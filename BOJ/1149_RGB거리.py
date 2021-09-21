# BOJ 1149 RGB 거리
import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lastR, lastG, lastB = arr[0]
for n in range(1, N):
    R = min(lastG, lastB) + arr[n][0]
    G = min(lastR, lastB) + arr[n][1]
    B = min(lastR, lastG) + arr[n][2]
    lastR, lastG, lastB = R, G, B
print(min(lastR, lastG, lastB))