import sys
sys.stdin = open('input.txt')
T = int(input()) # 테스트 케이스 개수
for tc in range(T):
    N = int(input()) # 카드의 장수
    nums = input() # 카드들을 문자열로 받음
    counts = [0] * 10 # 받은 카드의 수를 셀 리스트 초기화
    # 카드를 한장씩 확인하면서 카드의 숫자에 맞는 idx의 counts에 +1씩
    for i in range(N):
        counts[int(nums[i])] += 1
    cnt = counts[0] # 가장 많은 숫자의 카드 수 초기화
    for j in range(1, 10): # counts 리스트를 순회하며
        if counts[j] >= cnt: # 같은 경우 더 큰 숫자를 출력해야하므로 >가 아닌 >= 사용
            cnt = counts[j] # 더 큰 cnt
            max_cnt_num = j # 그때 해당하는 카드의 숫자
    print('#{} {} {}'.format(tc+1, max_cnt_num, cnt))