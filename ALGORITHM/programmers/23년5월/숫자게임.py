def solution(A, B):
    a = ans = 0
    A.sort()
    B.sort()
    for b in B:
        if b > A[a]:
            ans += 1
            a += 1
    return ans

print(solution([5,1,3,7], [2,2,6,8]))   # 3
print(solution([2,2,2,2], [1,1,1,1]))   # 0