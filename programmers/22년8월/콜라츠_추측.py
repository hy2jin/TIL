def solution(num):
    if num == 1:
        return 0
    cnt = 0
    while cnt < 500:
        cnt += 1
        if num % 2:
            num = num * 3 +1
        else:
            num /= 2
        if num == 1:
            return cnt
    return -1