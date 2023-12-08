# BOJ 9095 1, 2, 3 더하기
import sys
sys.stdin = open('input.txt')
'''
4 만들기
3 + 1 -> 만드는 법: dp[3]
2 + 2 -> 만드는 법: dp[2]
1 + 3 -> 만드는 법: dp[1]

5 만들기
4 + 1 -> 만드는 법: dp[4]
3 + 2 -> 만드는 법: dp[3]
2 + 3 -> 만드는 법: dp[2]
'''

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
for i in range(5, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(int(input())):
    print(dp[int(input())])
