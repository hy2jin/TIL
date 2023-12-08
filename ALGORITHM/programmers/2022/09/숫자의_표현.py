def solution(n):
    ans = 0
    for i in range(1, n+1):
        tmp = 0
        for j in range(i, n+1):
            tmp += j
            if tmp == n:
                ans += 1
                break
            elif tmp > n:
                break
    return ans