import sys
sys.stdin = open('input.txt')


def dfs(r, c, S):       # c는 필요없나..?
    global Minsum

    if r == N:          # 행을 다 봤고, 갱신이 필요하면 갱신
        if S < Minsum:
            Minsum = S
        return
    if S >= Minsum:     # 이미 합이 최소값보다 크면 더이상 볼 필요 X
        return

    for j in range(N):
        if not col[j]:  # 사용하지 않은 열이면
            col[j] = 1
            dfs(r+1, j, S + arr[r][j])  # 여기서 c가 필요한거 아닌가..?
            col[j] = 0


for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Minsum = N * 10     # 배열의 최소 합 초기화 / 10보다 작은 자연수 N개의 합
    S = 0               # 현재 합
    col = [0] * N       # 열 사용 여부
    dfs(0, 0, S)
    print('#{} {}'.format(tc+1, Minsum))
