import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    dir = 0 # 방향 0:오른, 1:아래, 2:왼, 3:위
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    cnt = 1 # 넣어줄 값
    r, c = 0, -1 # 출발하는 좌표
    while cnt <= N * N:
        nr, nc = r + dr[dir], c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            arr[nr][nc] = cnt
            cnt += 1
            r, c = nr, nc
        else:
            dir = (dir+1) % 4 # 방향 전환
    print('#{}'.format(tc+1))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()