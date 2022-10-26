# BOJ 1463 1로 만들기

N = int(input())            # 1 이상 10^6 이하인 정수
dp = [0] * (N+1)            # 0 때문에 N+1 까지

for i in range(2, N+1):     # dp[1] = 0 이니까 2부터 시작
    if i % 6 == 0:          # 2와 3 모두로 나눠떨어지면 둘 다 비교해야함
        dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i//3], dp[i-1]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i//2], dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1
print(dp[N])
