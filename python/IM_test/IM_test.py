import sys
sys.stdin = open('input.txt')


# def button(i):
#     change = [1, 0]
#     for idx in range(i, N+1, i):
#         led[idx] = change[led[idx]]


for tc in range(int(input())):
    N = int(input())
    led = [0]*(N+1)
    want = [0] + list(map(int, input().split()))
    change = [1, 0]
    cnt = 0
    for i in range(1, N+1):
        if led[i] != want[i]:
            for idx in range(i, N + 1, i):
                led[idx] = change[led[idx]]
            # button(i)
            cnt += 1
    print('#{} {}'.format(tc+1, cnt))
