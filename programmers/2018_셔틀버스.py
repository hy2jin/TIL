def solution(n, t, m, timetable):       # 셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한셔틀에 최대 m명
    answer = ''

    for i in range(len(timetable)):
        hr, mi = map(int, timetable[i].split(':'))
        timetable[i] = hr*60 + mi
    timetable.sort()        # 분으로 바꿔서 오름차순 정렬

    bus = []                # 셔틀버스 시간 분으로 표시
    for i in range(n):
        bus.append(9*60 + t*i)

    j = 0                   # 크루원들의 정류장 도착 idx
    for bs in bus:
        cnt = 0             # 몇명이 탔는가?
        while j < len(timetable) and timetable[j] <= bs:    # 버스보다 늦게오면 못탐
            cnt += 1
            j += 1
            if cnt == m:    # 버스 정원 꽉 차면 다음 버스
                break

        # 지금 이 버스를 타기 위한 방법
        if cnt < m:         # 버스에 빈 자리가 있으면 버스도착시간에 정류장 도착
            answer = bs
        else:               # 버스에 빈 자리가 없으면 마지막 사람보다 1분 빨리
            answer = timetable[j-1] - 1

    H, M = map(str, divmod(answer, 60))
    answer = H.zfill(2) + ':' + M.zfill(2)
    return answer

a = solution(2, 10, 2, ["09:10", "09:09", "08:00"])
print(a)
