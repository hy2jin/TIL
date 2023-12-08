# BOJ 2156 포도주 시식

n = int(input())
if n == 1:
    print(input())
else:
    wine = [0] + [int(input()) for _ in range(n)]
    dp = [0] * (n+1)
    dp[1] = wine[1]
    dp[2] = wine[2] + dp[1]
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], wine[i]+dp[i-2], wine[i]+wine[i-1]+dp[i-3])
    print(max(dp))