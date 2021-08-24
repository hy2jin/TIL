'''
* global 사용하지 않고 도착했는지 확인하기
* return 사용법
'''

import sys
sys.stdin = open('input.txt')
# 좌, 상, 우, 하
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def check(r, c):
    # 미로를 벗어나거나 벽이면 False / 갈 수 있는 길이면 True
    if r < 0 or (N-1) < r or c < 0 or (N-1) < c or arr[r][c] == '1':
        return False
    return True


def miro(r, c):
    visited[r][c] = 1
    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        if check(nr, nc) and visited[nr][nc] == 0:
            if arr[nr][nc] == '3':
                return 1
            # return 1을 받은적이 있으면 == 3을 찾은적이 있으면
            if miro(nr, nc):
                return 1
    return 0


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
    visited = [[0]*N for _ in range(N)]
    print('#{} {}'.format(tc+1, miro(sr, sc)))
