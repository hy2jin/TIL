# BOJ 2210 숫자판 점프
import sys
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(i, j, num):
    if len(num) == 6:
        if num not in number:
            number.append(num)
        return
    for d in range(4):
        ni, nj = i+dr[d], j+dc[d]
        if 0 <= ni < 5 and 0 <= nj < 5:
            dfs(ni, nj, num+arr[ni][nj])


sys.stdin = open('input.txt')
I = sys.stdin.readline
arr = [list(map(str, I().split())) for _ in range(5)]
number = []
for r in range(5):
    for c in range(5):
        dfs(r, c, arr[r][c])
print(len(number))