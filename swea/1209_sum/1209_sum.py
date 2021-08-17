import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for N in range(100)]
    sum_list = [] # 모든 합들을 담을 리스트
    d_sum = [0, 0] # [오른쪽아래로가는 대각선합, 왼쪽아래로가는 대각선 합]
    for r in range(100):
        rc_sum = [0, 0] # [행의 합, 열의 합]
        for c in range(100):
            rc_sum[0] += arr[r][c]
            rc_sum[1] += arr[c][r]
            if r == c:
                d_sum[0] += arr[r][c]
            if r + c == 99:
                d_sum[1] += arr[r][c]
        sum_list.extend(rc_sum) # 한 줄 구하면 합 리스트에 추가
    sum_list.extend(d_sum) # 대각선 다 더하면 합 리스트에 추가
    print('#{} {}'.format(tc, max(sum_list))) # 가장 큰 수 출력