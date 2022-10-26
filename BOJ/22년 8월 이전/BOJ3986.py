# BOJ 3986 좋은단어
import sys
sys.stdin = open('input.txt')
N = int(input())
cnt = 0
for _ in range(N):
    tmp = input()
    st = []
    for t in tmp:
        if not st or st[-1] != t:
            st.append(t)
        else:
            st.pop()
    if not st:
        cnt += 1
print(cnt)