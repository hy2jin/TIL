# BOJ 2491 수열
N = int(input())
nums = list(map(int, input().split()))
max_len = 1

# 증가
cnt = 1
for i in range(1, N):
    if nums[i] - nums[i-1] >= 0: cnt += 1
    else: cnt = 1
    if cnt > max_len: max_len = cnt         # 갱신
# 감소
cnt = 1
for j in range(1, N):
    if nums[j] - nums[j-1] <= 0: cnt += 1
    else: cnt = 1
    if cnt > max_len: max_len = cnt         # 갱신

print(max_len)