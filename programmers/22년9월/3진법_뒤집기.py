def solution(n):
    rev = ''
    while n > 0:
        n, m = divmod(n, 3)
        rev += str(m)
    return int(rev, 3)