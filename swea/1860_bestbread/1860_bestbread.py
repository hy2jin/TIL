import sys
sys.stdin = open('input.txt')
for tc in range(int(input())):
    N, M, K = map(int, input().split())     # N명의 손님, M초에 K개의 붕어빵
    cus = sorted(list(map(int, input().split())))
    ans = 'Possible'
    for i in range(N):
        bread = K * (cus[i] // M)           # 손님이 왔을때 붕어빵의 수
        if bread - i <= 0:                  # 앞에 다녀간 손님만큼 뺐을 때 0보다 커야지 빵을 살 수 있다.
            ans = 'Impossible'              # 0보다 작거나 같으면 빵을 살 수 없다.
            break
    print('#{} {}'.format(tc+1, ans))
