def check(num):
    for n in range(2, num):
        if num%n == 0:
            return False
    return True

def solution(nums):
    N = len(nums)
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                n = nums[i] + nums[j] + nums[k]
                if check(n):
                    ans += 1
    return ans