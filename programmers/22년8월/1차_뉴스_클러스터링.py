def solution(str1, str2):
    dic1, dic2 = {}, {}
    for i in range(len(str1)-1):
        tmp = str1[i:i+2].lower()
        if tmp.isalpha(): dic1[tmp] = dic1.get(tmp, 0) + 1
    for i in range(len(str2)-1):
        tmp = str2[i:i+2].lower()
        if tmp.isalpha(): dic2[tmp] = dic2.get(tmp, 0) + 1
    # print(dic1, dic2)
    inter = union = 0
    for k, v in dic1.items():
        union += v
        try: inter += min(v, dic2[k])
        except: pass
    for v in dic2.values(): union += v
    union -= inter
    if not union: return 65536
    return int(65536 * inter / union)