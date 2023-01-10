N = int(input())

if N == 1:
    print(0)
    exit()

isprime = [1 for _ in range(N + 1)]
isprime[0], isprime[1] = 0, 0
for i in range(2, int(N ** 0.5) + 1):
    if not isprime[i]: continue
    for j in range(i + i, N + 1, i):
        if isprime[j]: isprime[j] = 0

prime = [i for i in range(2, N + 1) if isprime[i]]

s, e, ans = 0, 0, 0
sub = prime[0]
while True:
    if sub > N:
        sub -= prime[s]
        s += 1
    else:
        if sub == N:
            ans += 1
        e += 1
        if e < len(prime):
            sub += prime[e]
        else:
            break

print(ans)
