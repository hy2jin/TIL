a, b = map(int, input().split())
x, y = map(int, input().split())

i = a*y + b*x
j = b*y

def GCD(a, b):
    if a > b:
        a, b = b, a
    while a:
        a, b = b%a, a
    return b

gcd = GCD(i, j)
print(i // gcd, j // gcd)