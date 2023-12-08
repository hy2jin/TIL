a, b = map(int, input().split())

isprime = [1] * (b + 1)
isprime[0] = isprime[1] = 0
for n in range(2, b + 1):
    if isprime[n]:
        for m in range(n + n, b + 1, n):
            isprime[m] = 0

def isunderprime(n):
    m = 2
    cnt = 0
    while n > 1:
        if n % m:
            m += 1
        else:
            n //= m
            cnt += 1
    return isprime[cnt]

ans = 0
for n in range(a, b + 1):
    if not isprime[n] and isunderprime(n):      # 소수는 길이가 소인수분해 길이가 1
        ans += 1

print(ans)
