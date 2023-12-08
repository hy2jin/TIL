def solution(record):
    answer = []
    dic = {}
    for rec in record:
        tmp = rec.split()
        if tmp[0] == "Change":
            dic[tmp[1]] = tmp[2]
        else:
            answer.append(tmp)
            if tmp[0] == "Enter":
                dic[tmp[1]] = tmp[2]

    for i in range(len(answer)):
        if answer[i][0] == "Enter":
            answer[i] = dic[answer[i][1]] + "님이 들어왔습니다."
        else:
            answer[i] = dic[answer[i][1]] + "님이 나갔습니다."

    return answer


a = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
print(a)