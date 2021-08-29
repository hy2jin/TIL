# BOJ 2559 수열
N, K = map(int, input().split())
nums = list(map(int, input().split()))
tmp = sum(nums[:K])
ans = tmp
for i in range(N-K):
    tmp += nums[i+K] - nums[i]
    ans = max(tmp, ans)
print(ans)