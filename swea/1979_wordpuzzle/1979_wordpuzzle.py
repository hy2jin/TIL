import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] # 퍼즐 만들기
    row = [] # 행 길이들의 리스트, 여기서 K의 수랑
    col = [] # 열 길이들의 리스트, 여기서 K의 수를 더한 값을 출력

    for r in range(N):
        row_v, col_v = 0, 0 # 흰색 행길이, 열길이 초기화
        for c in range(N):
            # 검은색을 만났는데, 이때까지 흰색 행의 길이 구한게 있으면
            if arr[r][c] == 0 and row_v:
                row.append(row_v) # 리스트에 길이 추가해주고
                row_v = 0 # 길이 리셋
            elif arr[r][c]:
                row_v += arr[r][c]

            # 검은색을 만났는데, 이때까지 흰색 열의 길이 구한게 있으면
            if arr[c][r] == 0 and col_v:
                col.append(col_v) # 리스트에 길이 추가해주고
                col_v = 0 # 길이 리셋
            elif arr[c][r]:
                col_v += arr[c][r]
        # 한줄 다 봤으면 길이 추가 (길이가 0이여도 어차피 나중에 count 안해줌)
        row.append(row_v)
        col.append(col_v)
    result = row.count(K) + col.count(K)

    print('#{} {}'.format(tc+1, result))