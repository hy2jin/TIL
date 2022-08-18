def solution(s):
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    ans = []
    for w in s:
        tmp = w.split(',')
        for t in tmp:
            if int(t) not in ans:
                ans.append(int(t))
                break
    return ans