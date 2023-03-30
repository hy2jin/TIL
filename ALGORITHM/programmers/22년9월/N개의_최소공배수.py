def lcm(x, y):
    c = x * y
    a, b = max(x, y), min(x, y)
    while a > 0:
        a, b = b%a, a
    return c/b

def solution(arr):
    LCM = arr[0]
    for n in arr:
        LCM = lcm(LCM, n)
    return LCM