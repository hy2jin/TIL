def solution(left, right):
    isOdd = [0]*1001
    for i in range(1, 32):
        isOdd[i**2] = 1
    ans = 0
    for n in range(left, right+1):
        if isOdd[n]:
            ans -= n
        else:
            ans += n
    return ans