# BOJ 13413 오셀로 재배치
import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    N = int(input())
    before = input()
    after = input()
    if before.count('W') == after.count('W'):
        cnt = 0
        for i in range(N):
            if before[i] != after[i]:
                cnt += 1
        print(cnt//2)
    else:
        W = B = 0
        for j in range(N):
            if before[j] != after[j]:
                if before[j] == 'W':
                    W += 1
                else:
                    B += 1
        print(max(B, W))
