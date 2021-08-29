import sys
sys.stdin = open('sample_input.txt')
for tc in range(int(input())):
    N, K = map(int, input().split())
    ok = list(map(int, input().split()))
    stu = list(range(1, N+1))
    for o in ok:
        stu.remove(o)
    print('#{} {}'.format(tc+1, ' '.join(map(str, stu))))