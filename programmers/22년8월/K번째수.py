def solution(array, commands):
    ans = []
    for i, j, k in commands:
        lst = sorted(array[i-1:j])
        ans.append(lst[k-1])
    return ans
