# BOJ 11650 좌표 정렬하기
import sys
sys.stdin = open('input.txt')

N = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(N)])
for l in lst:
    print(*l)