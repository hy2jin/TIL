# BOJ 2578 빙고

import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(5)]
check = []
for _ in range(5):
    check += list(map(int, input().split()))
# print(check)
R, C = [0]*5, [0]*5
D = [0, 0]
for i in range(25):
    a = False
    for r in range(5):
        for c in range(5):
            if arr[r][c] == check[i]:
                R[r] += 1
                C[c] += 1
                if r == c:
                    D[0] += 1
                if r + c == 4:
                    D[1] += 1
                a = True
                break
        if a: break
    if R.count(5) + C.count(5) + D.count(5) >= 3:
        break
print(i+1)