import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = []

    for i in range(N):
        if i%2: # 홀수번째에는 작은 수가 들어가야함
            min_idx = arr.index(min(arr))
            min_v = arr.pop(min_idx)
            sorted_arr.append(str(min_v))
            # 나중에 join 하려고 str()로 바꿔서 추가

        else: # 짝수번째에는 큰 수가 들어가야함
            max_idx = arr.index(max(arr))
            max_v = arr.pop(max_idx)
            sorted_arr.append(str(max_v))

    result = ' '.join(sorted_arr[:10]) # 10개만
    print('#{} {}'.format(tc+1, result))
