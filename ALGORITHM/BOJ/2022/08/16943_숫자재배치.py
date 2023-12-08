# BOJ 16943 숫자 재배치
import sys
import itertools
sys.stdin = open('input.txt')

A, B = map(str, input().split())
if len(A) > len(B):
    print(-1)
    exit()
A = list(map(str, A))
B = int(B)
C = list(itertools.permutations(A, len(A)))
ans = -1
for tmp in C:
    str_tmp = ''.join(tmp)
    c = int(''.join(tmp))
    if str(c) == str_tmp:
        if c < B:
            ans = max(ans, c)
print(ans)