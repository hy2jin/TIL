# BOJ 13300 방배정
import sys
sys.stdin = open('input.txt')
for _ in range(2):

    N, K = map(int, input().split())
    # 여학생 0 / 남학생 1
    room = [[0]*6, [0]*6]
    for _ in range(N):
        s, g = map(int, input().split())
        room[s][g-1] += 1

    cnt = 0
    for i in range(2):          # 성별 0, 1
        for j in room[i]:       # 해당 성별의 각 학년 학생 수
            # if j == 0: continue
            if j % K:
                cnt += j // K + 1
            else:
                cnt += j // K
    print(cnt)
