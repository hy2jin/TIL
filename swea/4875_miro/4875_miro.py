import sys
sys.stdin = open('input.txt')
# 좌 상 우 하
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def dfs(r, c):
    global ans
    if arr[r][c] == '3':
        ans = 1
        return
    visited.append((r, c))
    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '1' and (nr, nc) not in visited:
            dfs(nr, nc)
        if ans: break


for tc in range(int(input())):
    N = int(input())
    arr = []
    # 미로 만들기, 출발지 찾기
    find_s = False
    for i in range(N):
        tmp = input()
        arr.append(tmp)
        if not find_s and '2' in tmp:
            sr, sc = i, tmp.index('2')
            find_s = True
    # 방문 여부
    visited = []
    ans = 0
    dfs(sr, sc)
    print('#{} {}'.format(tc+1, ans))
