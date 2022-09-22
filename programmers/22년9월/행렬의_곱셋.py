def solution(arr1, arr2):
    ans = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for r in range(len(arr1)):
        for c in range(len(arr2[0])):
            for i in range(len(arr1[0])):
                ans[r][c] += arr1[r][i] * arr2[i][c]
    return ans

def solution(arr1, arr2):
    ans = [[sum(a * b for a, b in zip(a_row, b_col)) for b_col in zip(*arr2)] for a_row in arr1]
    return ans