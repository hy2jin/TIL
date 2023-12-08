N, M = map(int, input().split())
nums = list(map(int, input().split()))
tot = [nums[0]] * N
for i in range(1, N):
    tot[i] = tot[i-1] + nums[i]
tot = [0] + tot
for _ in range(M):
    a, b = map(int, input().split())
    print(tot[b] - tot[a-1])