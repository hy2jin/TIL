# BOJ 2851 슈퍼 마리오
import sys
sys.stdin = open('input.txt')

lst = [0] * 11
for i in range(1, 11):
    lst[i] = lst[i-1] + int(input())

s = b = 0
for j in range(1, 11):
    if lst[j] == 100:
        print(lst[j])
        exit()
    if lst[j] > 100:
        b = lst[j]
        break
    s = lst[j]

if b:
    S = 100 - s
    B = b - 100
    print(s) if S < B else print(b)
else:
    print(s)