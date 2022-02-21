# BOJ 9935 문자열 폭발
import sys
sys.stdin = open('input.txt')

inp = input()
bomb = input()
ans = []
L = len(bomb)

if len(bomb) == 1:
    for w in inp:
        if w != bomb:
            ans += w

else:
    for w in inp:
        ans += w

        a = ans[-1]
        b = bomb[-1]
        c = ''.join(ans[-L:])

        if a == b and c == bomb:
            for _ in range(L):
                ans.pop()

print(''.join(ans)) if ans else print('FRULA')
