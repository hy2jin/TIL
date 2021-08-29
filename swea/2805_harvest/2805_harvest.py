import sys
sys.stdin = open('input.txt')


def harvest(arr):
    global ans
    sp, w = N // 2, 1
    for nums in arr:
        for i in range(sp, sp + w):
            ans += int(nums[i])
        sp -= 1
        w += 2


for tc in range(int(input())):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans, half = 0, N//2                 # 반으로 쪼개서 위/아래 나눠서 더하기 위해
    harvest(arr[:half])                 # 윗부분
    harvest(arr[half:][::-1])           # 아랫부분 (제일 긴 부분 포함)
    print('#{} {}'.format(tc+1, ans))
