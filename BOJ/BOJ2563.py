# BOJ 2563 색종이

arr = [[0]*100 for _ in range(100)]
N = int(input())
cnt = 0
for _ in range(N):
    l, b = map(int, input().split())
    for r in range(l, l+10):
        for c in range(b, b+10):
            if arr[r][c] == 0:
                arr[r][c] = 1
                cnt += 1
print(cnt)
