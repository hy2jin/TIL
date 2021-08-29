# BOJ 10157 자리배정
R, C = map(int, input().split())
K = int(input())
arr = [[0]*C for _ in range(R)]
dr = [0, 1, 0, -1]      # 오른, 아래, 왼, 위
dc = [1, 0, -1, 0]
if R * C >= K:
    r, c = 0, -1
    n = 1               # 들어갈 숫자
    d = 0               # 0:오른, 1:아래, 2:왼, 3:위
    while n <= R*C:
        nr, nc = r+dr[d], c+dc[d]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 0:
            arr[nr][nc] = n
            if n == K:
                print(nr+1, nc+1)       # idx로 풀었으니 +1씩 해준다
                break
            n += 1
            r, c = nr, nc
        else:
            d = (d+1)%4
else:
    print(0)
