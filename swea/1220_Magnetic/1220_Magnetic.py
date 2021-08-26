import sys
sys.stdin = open('input.txt')
for tc in range(10):
    N = int(input())        # N x N 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for c in range(N):      # 한 열씩 확인
        r = 0
        while r < N:        # 0행 부터 (N-1)행까지
            if arr[r][c] == 1:              # 빨간색이면
                for i in range(r+1, N):
                    if arr[i][c] == 2:      # 그 밑으로 파란색이 있는지 확인
                        cnt += 1            # 있으면 교착상태 +1
                        r = i               # 행은 교착상태 위치로
                        break
            r += 1      # 행 +1
    print('#{} {}'.format(tc+1, cnt))
