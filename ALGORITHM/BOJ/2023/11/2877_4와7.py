N = int(input())
cnt = n = 0
nums = []
ans = ''

while True:
    n += 1
    cnt += 2**n
    if cnt >= N: break

idx = N - 2**n + 1
for _ in range(n):
    nums.append(idx % 2)
    idx //= 2
nums.reverse()

for i in range(len(nums)):
    if nums[i]:
        ans += '7'
    else:
        ans += '4'
print(ans)
