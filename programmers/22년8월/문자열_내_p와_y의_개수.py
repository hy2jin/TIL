def solution(s):
    p = y = 0
    for w in s:
        if w in 'pP': p += 1
        elif w in 'yY': y += 1
    if p != y:
        return False
    return True