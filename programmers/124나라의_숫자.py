def solution(n):
    if n < 4:
        return '124'[n-1]
    a, b = divmod(n-1, 3)
    return solution(a) + '124'[b]
