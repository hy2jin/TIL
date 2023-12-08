def solution(brown, yellow):
    N = brown + yellow
    candi = []
    for n in range(3, int(N**0.5) + 1):
        if N%n == 0:
            candi.append([N//n, n])
    
    for lst in candi:
        B = sum(lst)*2 - 4
        Y = lst[0] * lst[1] - B
        if B == brown and Y == yellow:
            return lst