def solution(answers):
    N = len(answers)
    a = [1, 2, 3, 4, 5] * (N//5 + 1)
    b = [2, 1, 2, 3, 2, 4, 2, 5] * (N//8 + 1)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (N//10 + 1)
    A, B, C = 0, 0, 0
    for i in range(N):
        if answers[i] == a[i]: A += 1
        if answers[i] == b[i]: B += 1
        if answers[i] == c[i]: C += 1
    M = max(A, B, C)
    ans = []
    if A == M: ans.append(1)
    if B == M: ans.append(2)
    if C == M: ans.append(3)
    return ans