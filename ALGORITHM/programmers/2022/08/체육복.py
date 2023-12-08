def solution(n, lost, reserve):
    cloth = [0] + [1] * n
    for lo in lost: cloth[lo] -= 1
    for re in reserve: cloth[re] += 1

    for i in range(1, n+1):
        if not cloth[i]:
            if cloth[i-1] == 2:
                cloth[i-1] -= 1
                cloth[i] += 1
            elif i < n and cloth[i+1] == 2:
                cloth[i+1] -= 1
                cloth[i] += 1

    cnt = 0
    for j in range(n+1):
        if cloth[j]:
            cnt += 1
    return cnt