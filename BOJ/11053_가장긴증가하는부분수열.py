# BOJ 11053 가장 긴 증가하는 부분 수열
import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))         # 수열
dp = [0] * N                    # idx까지 가장 긴 증가하는 부분수열 길이
for i in range(N):
    dp[i] = 1
    for j in range(i):          # 수열에서 앞의 숫자가 뒷 숫자보다 작고 j까지 증가하는 길이가 i까지 증가하는 길이보다 크면 dp[i]가 dp[j]보다 크도록
        if A[j] < A[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
