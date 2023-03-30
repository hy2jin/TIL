# BOJ 2941 크로아티아 알파벳
import sys
sys.stdin = open('input.txt')

word = input()
N = len(word)
i = cnt = 0
while i < N:
    if word[i] == 'd':
        if i < N-1 and word[i+1] == '-':
            i += 1
        elif i < N-2 and word[i+1] == 'z' and word[i+2] == '=':
            i += 2
    if word[i] == 'c' and i < N-1 and word[i+1] in '-=':
        i += 1
    elif word[i] == 'l' and i < N-1 and word[i+1] == 'j':
        i += 1
    elif word[i] == 'n' and i < N-1 and word[i+1] == 'j':
        i += 1
    elif word[i] == 's' and i < N-1 and word[i+1] == '=':
        i += 1
    elif word[i] == 'z' and i < N-1 and word[i+1] == '=':
        i += 1
    cnt += 1
    i += 1
print(cnt)