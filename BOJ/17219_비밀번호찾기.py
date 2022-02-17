# BOJ 17219 비밀번호 찾기
import sys
sys.stdin = open('input.txt')
I = sys.stdin.readline

N, M = map(int, I().split())
dic = {}
for i in range(N):
    u, p = I().split()
    dic[u] = p

for _ in range(M):
    url = I().rstrip()
    print(dic[url])