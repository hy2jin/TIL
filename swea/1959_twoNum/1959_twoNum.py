import sys
sys.stdin = open('input.txt')
for tc in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if M < N:       # A가 짧은게 되도록
        N, M = M, N
        A, B = B, A
    ans = 0
    for i in range(M-N+1):
        tmp = 0
        for j in range(N):
            tmp += A[j] * B[i+j]
        if tmp > ans:
            ans = tmp
    print('#{} {}'.format(tc+1, ans))
