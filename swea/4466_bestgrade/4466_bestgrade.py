import sys
sys.stdin = open('sample_input.txt')
for tc in range(int(input())):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)    # 내림차순 정렬하고 앞에서 K개의 합이 최대인 경우다
    print('#{} {}'.format(tc+1, sum(score[:K])))
