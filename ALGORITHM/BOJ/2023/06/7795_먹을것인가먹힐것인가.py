import sys
sys.stdin = open('i.txt')

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(); B.sort();

    # 투포인터
    ans = b = 0
    for a in range(N):
        while b < M and A[a] > B[b]:
            b += 1
        ans += b
    print(ans)


    # # 이진탐색
    # ans = 0
    # for a in range(N):
    #     left = 0; right = M;
    #     while left + 1 < right:
    #         mid = (left + right) // 2
    #         if A[a] > B[mid]: left = mid
    #         else: right = mid

    #     ans += left
    #     if A[a] > B[left]: ans += 1
    # print(ans)


    # # 완전탐색
    # ans = 0
    # for a in range(N):
    #     for b in range(M):
    #         if A[a] > B[b]: ans += 1
    #         else: break
    # print(ans)
