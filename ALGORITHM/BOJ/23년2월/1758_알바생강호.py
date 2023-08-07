N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

ans = sum([max(arr[i] - i, 0) for i in range(N)])
print(ans)
