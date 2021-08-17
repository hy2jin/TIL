import sys
sys.stdin = open('input.txt')
T = int(input()) # 테스트 케이스의 개수
for tc in range(T):
    N, M = map(int, input().split()) # N개의 정수들의 배열, 이웃한 M개의 합
    nums = list(map(int, input().split()))
    max_case, min_case = sum(nums[:M]), sum(nums[:M])
    # nums[start:end]에서 start가 전체 리스트 길이에서 M-1을 뺀것까지
    for i in range(1, N-M+1):
        if sum(nums[i:i+M]) > max_case:
            max_case = sum(nums[i:i+M])
        if sum(nums[i:i+M]) < min_case:
            min_case = sum(nums[i:i+M])
    print('#{} {}'.format(tc+1, max_case - min_case))