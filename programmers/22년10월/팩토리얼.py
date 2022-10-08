def solution(n):
    if n < 2:
        return n
    fac = 1
    for i in range(1, 11):
        if fac < n:
            fac *= i
        elif fac == n:
            return i-1
        else:
            return i-2