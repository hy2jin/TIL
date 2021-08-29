# BOJ 2491 수열
N = int(input())
nums = list(map(int, input().split()))
max_len = 1

# 증가 감소 한번에
cnt1, cnt2 = 1, 1
for i in range(1, N):
    # 증가
    if nums[i] - nums[i-1] >= 0: cnt1 += 1
    else: cnt1 = 1
    if cnt1 > max_len: max_len = cnt1
    # 감소
    if nums[i] - nums[i-1] <= 0: cnt2 += 1
    else: cnt2 = 1
    if cnt2 > max_len: max_len = cnt2

# # 증가
# cnt = 1
# for i in range(1, N):
#     if nums[i] - nums[i-1] >= 0: cnt += 1
#     else: cnt = 1
#     if cnt > max_len: max_len = cnt         # 갱신
# # 감소
# cnt = 1
# for j in range(1, N):
#     if nums[j] - nums[j-1] <= 0: cnt += 1
#     else: cnt = 1
#     if cnt > max_len: max_len = cnt         # 갱신

print(max_len)