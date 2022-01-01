# BOJ 2579 계단 오르기
import sys
sys.stdin = open('input.txt')
'''
n번째 계단의 dp값
1. n번째 계단이 연속된 1번째인 경우
-> lst[n] + dp[n-2]
2. n번째 계단이 연속된 2번째인 경우
-> lst[n] + lst[n-1] + dp[n-3]
'''
N = int(input())
if N == 1:              # lst[2]값이 있을 수 없다 -> index error
    print(input())
else:
    lst = [0] + [int(input()) for _ in range(N)]
    dp = [0] * (N+1)
    dp[1] = lst[1]
    dp[2] = lst[2] + dp[1]
    for i in range(3, N+1):
        dp[i] = max(lst[i]+dp[i-2], lst[i]+lst[i-1]+dp[i-3])
    print(dp[-1])
