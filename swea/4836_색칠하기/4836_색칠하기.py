import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    arr = [[0]*10 for _ in range(10)]
    N = int(input()) # 색칠 몇번
    cnt = 0 # 겹친 수

    for i in range(N):
        a, b, c, d, color = map(int, input().split())
        for r in range(a, c+1):
            for c in range(b, d+1):
                if arr[r][c] != color:
                    arr[r][c] += color

    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                cnt += 1
    print('#{} {}'.format(tc+1, cnt))
