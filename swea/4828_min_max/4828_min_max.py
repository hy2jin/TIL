import sys
sys.stdin = open('input.txt')
T = int(input()) # 테스트 케이스의 수
for tc in range(T):
    N = int(input()) # 양수의 개수
    nums = list(map(int, input().split())) # 양수들의 리스트
    num_max, num_min = nums[0], nums[0] # 가장 큰 수와 가장 작은 수 초기화
    for i in range(1, N):
        if nums[i] > num_max:
            num_max = nums[i]
        if nums[i] < num_min:
            num_min = nums[i]
    print('#{} {}'.format(tc+1, num_max - num_min))