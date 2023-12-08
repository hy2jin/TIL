# BOJ 17413  단어 뒤집기 2
import sys
sys.stdin = open('input.txt')

S = input()
L = len(S)
i = 0
ans = ''
while i < L:
    if S[i] == '<':
        s = i
        while S[i] != '>':
            i += 1
        i += 1
        ans += S[s:i]
    elif S[i] != ' ':
        s = i
        while i < L and S[i] != ' ' and S[i] != '<':
            i += 1
        ans += S[s:i][::-1]
    else:
        ans += ' '
        i += 1
print(ans)
