# BOJ 16926 배열 돌리기1
import sys
sys.stdin = open('16927.txt')

# 하, 우, 상, 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
new = [[0]*M for _ in range(N)]

for i in range(R):
    # 아래로, 오른쪽으로, 위로, 왼쪽으로 몇번 옮길까?
    move = [N-1, M-1, N-1, M-1]
    r, c = 0, 0         # 시작
    d = 0
    while min(move) > 0:
        cnt = move[d]
        while cnt > 0:
            nr, nc = r+dr[d], c+dc[d]
            new[nr][nc] = arr[r][c]
            r, c = nr, nc
            cnt -= 1
        d += 1

        if d > 3:       # 한바퀴 다 돌았음
            d = 0       # 다시 아래쪽부터
            for m in range(4):
                move[m] -= 2    # 갈 수 있는 횟수가 2씩 줄어든다
            r += 1      # 시작위치: (0, 0) -> (1, 1) -> (2, 2) -> ...
            c += 1
    if i < R-1:         # 마지막을 제외하고 다시 돌리기 위해 arr을 new로 덮어쓴다
        arr = [new[j][:] for j in range(N)]

for ne in new:
    print(' '.join(map(str, ne)))
