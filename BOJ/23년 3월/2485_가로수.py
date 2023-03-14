def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

N = int(input())
prev = int(input())
terms = []
for _ in range(N - 1):
    cur = int(input())
    terms.append(abs(cur - prev))
    prev = cur

gcd = terms[0]
for i in range(1, len(terms)):
    gcd = GCD(gcd, terms[i])

ans = 0
for term in terms:
    ans += term // gcd - 1

print(ans)
