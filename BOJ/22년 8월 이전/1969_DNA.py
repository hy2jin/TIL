# BOJ 1969 DNA

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
data = [input() for _ in range(N)]
data.sort()

dna = ''
for j in range(M):
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(N):
        acgt = data[i][j]
        dic[acgt] += 1
    dna += max(dic, key=dic.get)

cnt = 0
for i in range(N):
    for j in range(M):
        if data[i][j] != dna[j]:
            cnt += 1

print(dna)
print(cnt)
