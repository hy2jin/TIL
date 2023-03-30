def solution(arr):
    ans = []
    for n in arr:
        if not ans or ans[-1] != n:
            ans.append(n)
    return ans