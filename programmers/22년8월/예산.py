def solution(d, budget):
    d.sort()
    ans = 0
    for n in d:
        budget -= n
        if budget >= 0:
            ans += 1
        else:
            break
    return ans