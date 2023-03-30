def solution(participant, completion):
    dic = {}
    for parti in participant:
        dic[parti] = dic.get(parti, 0) + 1
    for com in completion:
        dic[com] -= 1
    for k, v in dic.items():
        if v:
            return k