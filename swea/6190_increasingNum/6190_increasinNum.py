import sys
sys.stdin = open('s_input.txt')


def check(num):
    number = str(num)       # 숫자 하나씩 비교하기 위해 형변환
    for k in range(len(number)-1):
        if number[k] > number[k+1]:
            return 0        # 앞 숫자가 더 크면 return 0
    return 1                # 뒷 숫자가 더 크면 return 1


for tc in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = 0     # 단조 증가하는 수의 최대값을 갱신해줄 변수
    cnt = 0     # 단조 증가하는 수가 있는지 없는지 판단하기 위한 변수

    # 모든 경우의 수 다 탐색하기 위한 이중 for문
    for i in range(N-1):
        for j in range(i+1, N):
            tmp = nums[i] * nums[j]
            if check(tmp):                  # 단조 증가하는 수인가?
                cnt += 1
                if tmp > ans: ans = tmp     # 최대값이면 갱신
    if not cnt: ans = -1    # cnt == 0이면 단조 증가하는 수가 없다는 뜻이므로 -1 출력
    print('#{} {}'.format(tc+1, ans))
