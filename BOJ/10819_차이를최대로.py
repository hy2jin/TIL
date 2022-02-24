# BOJ 10819 차이를 최대로
import sys
sys.stdin = open('input.txt')

def calc():
    global ans
    tmp = 0
    for i in range(N-1):
        tmp += abs(A[lst[i]] - A[lst[i+1]])
    if tmp > ans: ans = tmp

def recur(idx):
    if idx == N:
        calc()
        return
    for i in range(N):
        if i not in lst:
            lst[idx] = i
            recur(idx+1)
            lst[idx] = -1

N = int(input())
A = list(map(int, input().split()))
lst = [-1] * N
ans = 0
for i in range(N):
    lst[0] = i
    recur(1)
    lst[0] = -1
print(ans)