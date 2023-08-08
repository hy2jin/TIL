https://www.acmicpc.net/problem/28432

N = int(input())
arr = []
for i in range(N):
    arr.append(input())
    if arr[i] == '?':
        idx = i

M = int(input())
for _ in range(M):
    can = input()
    if idx > 0 and can[0] != arr[idx - 1][-1]:
        continue
    if idx < len(arr) - 1 and can[-1] != arr[idx + 1][0]:
        continue
    if can not in arr:
        print(can)
        break
