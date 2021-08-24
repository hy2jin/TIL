import sys
sys.stdin = open('input.txt')
# 좌, 상, 우, 하
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def miro(r, c):
    global ans
    if arr[r][c] == '3':        # 도착
        ans = 1
        return
    if ans: return              # 도착을 찾음

    visited.append((r, c))
    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '1' and (nr, nc) not in visited:
            miro(nr, nc)


for tc in range(int(input())):
    N = int(input())
    arr = []
    # 미로 만들기, 출발점 찾기
    find_sc = False
    for i in range(N):
        tmp = input()
        arr.append(tmp)
        if not find_sc and '2' in tmp:
            sr, sc = i, tmp.index('2')
            find_sc = True
    ans = 0
    visited = []
    miro(sr, sc)
    print('#{} {}'.format(tc+1, ans))
