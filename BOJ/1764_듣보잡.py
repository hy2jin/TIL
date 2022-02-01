# BOJ 1764 듣보잡
'''
문제를 똑바로 안읽어서 길이 출력을 안해줘서 틀림
'''
import sys
sys.stdin = open('input.txt')
I = sys.stdin.readline
N, M = map(int, I().split())
chk = set()
for _ in range(N):
    chk.add(I().rstrip())
ans = []
for _ in range(M):
    tmp = I().rstrip()
    if tmp in chk:
        ans.append(tmp)
print(len(ans))
for a in sorted(ans):
    print(a)