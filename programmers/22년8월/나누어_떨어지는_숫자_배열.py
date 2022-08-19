def solution(arr, divisor):
    ans = sorted([n for n in arr if not n%divisor]) or [-1]
    return ans