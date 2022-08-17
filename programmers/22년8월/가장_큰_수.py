def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=lambda x:x*3, reverse=True)
    ans = int(''.join(nums))
    return str(ans)