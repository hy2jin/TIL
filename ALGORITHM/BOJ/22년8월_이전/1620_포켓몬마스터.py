# BOJ 1620 나는야 포켓몬 마스터 이다솜
import sys
sys.stdin = open('input.txt')
I = sys.stdin.readline

N, M = map(int, I().split())
po = [''] + [I().strip() for _ in range(N)]
for _ in range(M):
    tmp = I().strip()
    try:
        print(po[int(tmp)])
    except:
        print(po.index(tmp))
