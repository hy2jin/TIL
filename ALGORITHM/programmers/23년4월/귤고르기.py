from collections import OrderedDict

def solution(k, tangerine):
    dic = {}
    for t in tangerine:
        try: dic[t] += 1
        except: dic[t] = 1
    oDic = OrderedDict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
    kList = list(oDic)

    for i in range(len(kList)):
        k -= dic[kList[i]]
        if k <= 0:
            return i + 1
