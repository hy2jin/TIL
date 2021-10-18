# BOJ 11722 가장 긴 감소하는 부분 수열
import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[j] > A[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
