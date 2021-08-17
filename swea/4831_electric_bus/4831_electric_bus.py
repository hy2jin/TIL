import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    # K : 한번 충전으로 갈수있는 정류장수
    # N : 종점
    # M : 충전기가 설치된 정류장 수
    chrg_stations = list(map(int, input().split())) # 충전기가 설치된 정류장들
    # 충전 가능한 정류장 표시하기
    stations = [0] * N
    for i in chrg_stations:
        stations[i] = 1
    # print(chrg_stations)
    cnt, bus_start = 0, stations[0]
    while True:
        for i in range(bus_start + K, bus_start, -1):
            if stations[i]:
                cnt += 1
                bus_start = i
                break
        # for문에서 break하지 않았다는 것은 충전소 도착전에 버스가 멈췄다는 것
        # cnt는 0으로 하고 그대로 끝
        else:
            cnt = 0
            break
        # 더 이상의 충전없이 도착 가능하면 그대로 끝
        if bus_start + K >= N:
            break
    print('#{} {}'.format(tc+1, cnt))
