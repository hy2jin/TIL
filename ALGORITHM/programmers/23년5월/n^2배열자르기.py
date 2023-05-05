def solution(n, left, right):
    arr = []
    for i in range(left, right + 1):
        r, c = divmod(i, n)
        arr.append(max(r, c) + 1)
    return arr
