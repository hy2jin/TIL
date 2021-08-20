import sys
sys.stdin = open('input.txt')
T = int(input())
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(T):
    N, K = map(int, input().split()) # N:부분집합 원소의 수
    cnt = 0 # 부분집합 합이 K인 경우의 개수

    for i in range(1, 1<<12): # 부분집합의 개수만큼 (2의 12제곱만큼)
        sub_sum = 0 # 부분집합의 합
        subset = [] # 부분집합

        for j in range(12): # 부분집합원소가 0개일때부터 12개일때까지
            if i & (1<<j): # i의 j번째 비트가 1이면
                sub_sum += arr[j]
                subset.append(arr[j])

        if len(subset) == N and sub_sum == K:
            cnt += 1

    print('#{} {}'.format(tc+1, cnt))
