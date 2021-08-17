import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    n = int(input()) # 가능한 덤프 횟수
    box = list(map(int, input().split())) # 상자의 높이
    # max(), min() 있는 ver
    while n > 0:
        max_h, min_h = max(box), min(box)
        max_idx, min_idx = box.index(max_h), box.index(min_h)
        box[max_idx] -= 1
        box[min_idx] += 1
        n -= 1
    print('#{} {}'.format(tc, max(box) - min(box)))

    '''
    # max(), min() 없는 ver
    while n > 0:
        max_idx, min_idx = 0, 0 # 최고점, 최저점의 index 초기화
        max_h, min_h = box[0], box[0] # 최고점, 최저점의 높이 초기화
        for i in range(1, len(box)):
            if box[i] > max_h:
                max_h = box[i]
                max_idx = i
            if box[i] < min_h:
                min_h = box[i]
                min_idx = i
        box[max_idx] -= 1
        box[min_idx] += 1
        n -= 1
        print('#{} {}'.format(tc, max(box) - min(box)))
    '''
