# BOJ 2304 창고 다각형
'''
arr = sorted(arr, key=lambda lst: lst[0])
arr을 arr원소의 [0]으로 정렬한다
'''
import sys
sys.stdin = open('input.txt')

N = int(input())
# 높이를 담을 배열 (최대 1000, idx 접근)
H = [0] * 10001
# 가로 최대, 세로 최대
max_x, max_y = 0, 0
for _ in range(N):
    x, y = map(int, input().split())
    H[x] = y
    if max_x < x:
        max_x = x
    if max_y < y:
        max_y = y
        max_idx = x     # 세로최대일때 가로값

ans = 0
# 왼쪽
left = H[0]
for i in range(max_idx+1):      # 최대 높이 포함
    if H[i] > left:
        left = H[i]
    ans += left

# 오른쪽
right = H[-1]
for i in range(max_x, max_idx, -1):
    if H[i] > right:
        right = H[i]
    ans += right

print(ans)
