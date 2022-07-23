def solution(nums):
    N = len(nums)
    uniqN = len(set(nums))
    if uniqN > N//2:
        return N//2
    else:
        return uniqN