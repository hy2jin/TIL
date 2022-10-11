def solution(s):
    a = b = 0
    while s != "1":
        a += 1
        L = s.count("1")
        b += len(s) - L
        s = bin(L)[2:]
    return [a, b]