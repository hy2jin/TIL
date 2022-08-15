def solution(n):
    m = n**0.5
    if int(m) == m:
        return (m+1)**2
    return -1