def solution(name, yearning, photo):
    # dic = { name[i]: yearning[i] for i in range(len(name)) }
    dic = dict(zip(name, yearning))

    for i in range(len(photo)):
        s = 0
        for n in photo[i]:
            try: s += dic[n]
            except: pass
        photo[i] = s
    return photo