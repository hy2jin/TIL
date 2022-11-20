"""
1. 오름차순
    => 입력받으면 바로 정렬해주기
2. N개의 자연수는 모두 다른 수
    => idx만 보고, 숫자의 중복 생각할 필요X
"""

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = [0] * M


def dfs(si, idx):
    if idx == M:
        print(" ".join(map(str, ans)))
        return
    
    for j in range(si, N):
        ans[idx] = nums[j]
        dfs(j + 1, idx + 1)


for i in range(N):
    ans[0] = nums[i]
    dfs(i + 1, 1)
