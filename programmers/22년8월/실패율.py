def solution(N, stages):
    now = [0] * (N+2)               # idx: 스테이지넘버, now[idx]: 몇명이 있는가
    for st in stages:
        now[st] += 1

    cnt = now[N+1]                  # 실패율 계산시 분모
    fail = [0] * (N+1)              # 실패율 배열
    for n in range(N, 0, -1):
        if now[n]:
            cnt += now[n]
            fail[n] = now[n]/cnt

    tmp = [[i, f] for i, f in enumerate(fail) if i]     # 스테이지넘버(0 제외)와 실패율 묶음
    tmp.sort(key = lambda x:-x[1])  # 실패율이 높은 순으로 정렬
    ans = [i[0] for i in tmp]       # 실패율만 뽑아낸 배열

    return ans