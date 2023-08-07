N, K = map(int, input().split())
arr = list(map(int, input().split()))

i, j, ans = 0, 0, 0
dic = {}

while j < N:
    if dic.get(arr[j], 0) < K:
        dic[arr[j]] = dic.get(arr[j], 0) + 1
        j += 1
    else:
        dic[arr[i]] -= 1
        i += 1
    
    ans = max(ans, j - i)

print(ans)
