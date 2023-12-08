def solution(s, n):
    a = 'abcdefghijklmnopqrstuvwxyz'
    A = a.upper()
    ans = ''
    for w in s:
        if w == ' ':
            ans += ' '
        elif w.islower():
            i = a.index(w)
            ans += a[(i+n)%26]
        else:
            i = A.index(w)
            ans += A[(i+n)%26]
    return ans