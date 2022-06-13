def solution(arr1, arr2):
    answer = [[arr1[r][c] + arr2[r][c] for c in range(len(arr1[0]))] for r in range(len(arr1))]
    return answer