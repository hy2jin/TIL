arr = [[0] * 15 for _ in range(15)]

for i in range(15):
    for j in range(1, 15):
        if i == 0:                                  # 0층 j호에는 j명이 있다
            arr[i][j] = j
            continue

        arr[i][j] = arr[i][j - 1] + arr[i - 1][j]   # 0층 말고는 dp

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    print(arr[k][n])                                # 바로 출력
