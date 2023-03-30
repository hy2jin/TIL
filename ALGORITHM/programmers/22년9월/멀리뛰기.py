def solution(n):
    if n < 4:
        return n
    a = b = 1
    for _ in range(n):
        a, b = b, a+b
    return a%1234567