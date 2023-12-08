def solution(lines):
    arr = [0] * 202
    for line in lines:
        for i in range(line[0], line[1]):
            arr[i + 100] += 1
    ans = 0
    for i in range(len(arr)):
        if arr[i] > 1:
            ans += 1
    return ans