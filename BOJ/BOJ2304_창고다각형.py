# BOJ 2304 창고 다각형
'''
* 포인트
arr = sorted(arr, key=lambda lst: lst[0])
arr을 arr원소의 [0]으로 정렬한다
'''
import sys
sys.stdin = open('input.txt')

N = int(input())
MaxL, MaxH = 0, 0
lastMaxL, lastMasH = 0, 0
arr = []
for _ in range(N):
    L, H = map(int, input().split())
    if H > MaxH:
        MaxL, MaxH = L, H
    if H >= MaxH:
        lastMaxL, lastMaxH = L, H
    arr.append([L, H])

# 최고높이의 왼쪽과 오른쪽으로 나눠서 계산하기위해 정렬
arr = sorted(arr, key=lambda lst: lst[0])

# 제일 높은게 여러개라면..?
area = (lastMaxL - MaxL + 1) * MaxH

# 왼쪽
l, h = arr[0]
i = 1
while arr[i][0] <= MaxL:
    if arr[i][1] > h:
        area += (arr[i][0] - l) * h
        l, h = arr[i]
    i += 1

# 오른쪽
l, h = arr[N-1]
i = N-2
while arr[i][0] >= lastMaxL:
    if arr[i][1] > h:
        area += (l - arr[i][0]) * h
        l, h = arr[i]
    i -= 1
print(area)
