def solution(progresses, speeds):
    answer = []
    lst = []
    for i in range(len(speeds)):
        a, b = divmod(100-progresses[i], speeds[i])
        if b:
            lst = [a+1] + lst
        else:
            lst = [a] + lst
    tmp = []
    while lst:
        n = lst.pop()
        if not tmp or tmp[0] >= n:
            tmp.append(n)
        else:
            answer.append(len(tmp))
            tmp = [n]
    answer.append(len(tmp))
    return answer