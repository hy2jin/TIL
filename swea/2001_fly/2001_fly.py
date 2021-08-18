import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    fly_sum = [] # 파리들의 합을 담고 나중에 여기서 최대값을 출력함

    for r in range(N-M+1): # 파리채 크기 생각해서 범위 설정
        for c in range(N-M+1):

            v = 0 # 파리들의 합을 담을 변수
            for i in range(M): # 파리채로 파리들이 죽을 범위
                for j in range(M):
                    v += arr[r+i][c+j]
            fly_sum.append(v)

    print('#{} {}'.format(tc+1, max(fly_sum)))
