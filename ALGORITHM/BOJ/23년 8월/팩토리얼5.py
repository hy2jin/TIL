# https://www.acmicpc.net/problem/1564

N = int(input())
ans = 1
for i in range(2, N + 1):
    ans *= i
    while ans % 10 == 0:
        ans //= 10
    ans %= 100000000000000000

print(str(ans)[-5:])
