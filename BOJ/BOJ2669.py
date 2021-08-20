# BOJ 2669 직사각형 네개의 합집합 면적

square = [list(map(int, input().split())) for _ in range(4)]
arr = [[0]*100 for _ in range(100)]
cnt = 0
for i in range(4):
    for r in range(square[i][1], square[i][3]):
        for c in range(square[i][0], square[i][2]):
            # 빈곳을 채울때만 count해주면 따로 for문을 쓸 필요가 없음
            if not arr[r][c]:
                arr[r][c] = 1
                cnt += 1
print(cnt)