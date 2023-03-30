def solution(absolutes, signs):
    ans = 0
    for i, v in enumerate(signs):
        if v:
            ans += absolutes[i]
        else:
            ans -= absolutes[i]
    return ans