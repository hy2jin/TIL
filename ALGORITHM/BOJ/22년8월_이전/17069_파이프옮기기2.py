# BOJ 17069 파이프 옮기기 2
import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
cnt[0][1][0] = 1            # cnt[i][j][d] : d방향 파이프가 i, j에 도달하는 방법의 수
# d --> 0:가로, 1:대각선, 2:세로
for i in range(N):
    for j in range(2, N):   # 이게 2부터 시작하는게 중요!!
        if arr[i][j] == 0:
            cnt[i][j][0] = cnt[i][j-1][0] + cnt[i][j-1][1]
            if i - 1 >= 0:
                cnt[i][j][2] = cnt[i-1][j][1] + cnt[i-1][j][2]
                if arr[i][j-1] == 0 and arr[i-1][j] == 0:
                    cnt[i][j][1] = cnt[i-1][j-1][0] + cnt[i-1][j-1][1] + cnt[i-1][j-1][2]

print(cnt[-1][-1][0] + cnt[-1][-1][1] + cnt[-1][-1][2])
