def solution(n, m, section):
    wall = [0] * (n + 1)
    for s in section:
        wall[s] = 1
    ans = 0
    for s in section:
        if wall[s] == 0: continue
        for i in range(s, s + m):
            if i < n + 1:
                wall[i] = 0
            else:
                break
        ans += 1
    return ans
