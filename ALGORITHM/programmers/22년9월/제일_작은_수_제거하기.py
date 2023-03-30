def solution(arr):
    m = min(arr)
    ans = [n for n in arr if n > m]
    return ans if ans else [-1]