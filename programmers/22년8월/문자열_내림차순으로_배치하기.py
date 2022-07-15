def solution(s):
    ans = sorted(list(s), reverse=True)
    return ''.join(ans)