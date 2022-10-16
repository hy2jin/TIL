def solution(cipher, code):
    ans = ''
    for i, v in enumerate(cipher):
        if (i+1) % code == 0:
            ans += v
    return ans