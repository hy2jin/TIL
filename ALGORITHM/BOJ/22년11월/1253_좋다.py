N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

# for i in range(N):
#     l, r = 0, N - 1
#     while l < r:
#         if l == i:
#             l += 1
#             continue
#         if r == i:
#             r -= 1
#             continue
#         total = arr[l] + arr[r]
#         if total == arr[i]:
#             ans += 1
#             break
#         elif total < arr[i]:
#             l += 1
#         else:
#             r -= 1

for i in range(N):
    lst = arr[:i] + arr[i+1:]
    l, r = 0, N - 2

    while l < r:
        total = lst[l] + lst[r]
        if total == arr[i]:
            ans += 1
            break
        elif total < arr[i]:
            l += 1
        else:
            r -= 1

print(ans)