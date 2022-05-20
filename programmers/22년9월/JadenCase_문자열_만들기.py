def solution(s):
    ans = s[0].upper()
    for i in range(1, len(s)):
        if s[i].isalpha():
            if s[i-1] == ' ':
                ans += s[i].upper()
            else:
                ans += s[i].lower()
        else:
            ans += s[i]
    return ans