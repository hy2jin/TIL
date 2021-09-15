# BOJ 2504 괄호의 값
import sys
sys.stdin = open('input.txt')
g_set = {')': '(', ']': '['}


def is_pair(G):     # 쌍이 맞는가?
    st = []
    for g in G:
        if g in '([': st.append(g)
        elif st[-1] == g_set[g]: st.pop()
        else: return 0
    if st: return 0
    else: return 1


def cal(G):
    st = []
    for g in G:
        if g in '([': st.append(g)
        el


G = input()
if is_pair(G):
    st = []
    for i in range(len(G)):
        if G[i] in '([': st.append(G[i])
        elif G[i] in ']'
else:
    ans = 0