# BOJ 1292 쉽게 푸는 문제

a, b = map(int, input().split())
lst = []
n = 1
while len(lst) < b:
    lst += [n] * n
    n += 1
print(sum(lst[a-1:b]))