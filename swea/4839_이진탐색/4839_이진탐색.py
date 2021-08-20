import sys
sys.stdin = open('input.txt')
T = int(input())

def binary_search(p, key):
    l, r = 1, p
    cnt = 0
    while l <= r:
        c = (l+r)//2
        if c == key:
            return cnt
        elif c < key:
            l = c
        else:
            r = c
        cnt += 1

for tc in range(T):
    P, A, B = map(int, input().split())
    A_cnt = binary_search(P, A)
    B_cnt = binary_search(P, B)
    if A_cnt < B_cnt:
        res = 'A'
    elif A_cnt > B_cnt:
        res = 'B'
    else:
        res = 0
    print('#{} {}'.format(tc+1, res))
