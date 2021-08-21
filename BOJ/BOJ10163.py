# BOJ 10163 색종이
N = int(input())
arr = [[0]*1001 for _ in range(1001)]
cnt = [0]*N
for i in range(1, N+1):
    r, c, dr, dc = map(int, input().split())
    for j in range(r, r+dr):
        for k in range(c, c+dc):
            if arr[j][k] == 0:
                arr[j][k] = i
            else:
                cnt[arr[j][k]-1] -= 1
                arr[j][k] = i
            cnt[i-1] += 1
for a in range(N):
    print(cnt[a])