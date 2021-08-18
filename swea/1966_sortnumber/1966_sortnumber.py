import sys
sys.stdin = open('input.txt')

# 선택정렬
def selection_sort(arr):
    # 처음부터 마지막에서 하나 전까지 제일 작은값들을 차례대로 넣어주면 마지막은 가장 큰게 됨
    for i in range(len(arr)-1):
        min_idx = i # 시작이 제일 작다고 치고 업데이트 해주기
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = selection_sort(arr)
    result = ' '.join(map(str, sorted_arr))
    print('#{} {}'.format(tc+1, result))