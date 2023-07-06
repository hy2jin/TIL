def solution(code):
    ans = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode = (mode + 1) % 2
            continue
        if mode == i % 2:
            ans += code[i]

    return ans if ans else 'EMPTY'
