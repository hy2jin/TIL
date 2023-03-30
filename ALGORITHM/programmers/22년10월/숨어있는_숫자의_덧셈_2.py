def solution(my_string):
    ans = 0
    num = ''
    for s in my_string:
        if s.isdigit():
            num += s
        elif num:
            ans += int(num)
            num = ''
    return ans + int(num) if num else ans
