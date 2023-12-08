def solution(a, b):
    ans = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]

    cnt = b - 1
    for i in range(a - 1):
        cnt += month[i]
    
    return ans[cnt % 7]
