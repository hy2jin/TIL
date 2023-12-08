def solution(x):
    S = 0
    for i in str(x):
        S += int(i)
    return x % S == 0