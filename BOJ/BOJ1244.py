# BOJ 1244 스위치 켜고 끄기
import sys
sys.stdin = open('input.txt')
N = int(input())        # N개의 스위치
switch = list(map(int, input().split()))
M = int(input())        # M명의 학생
student = [list(map(int, input().split())) for _ in range(M)]
change = [1, 0]         # idx 접근으로 0이면 1로, 1이면 0으로 바꾸기

for s in student:
    gen, sp = s
    if gen == 1:       # 남학생
        for i in range(sp-1, N, sp):            # 스위치번호-1 == idx
            switch[i] = change[switch[i]]       # idx로 접근해서 스위치상태를 바꿔줘야함

    else:               # 여학생
        switch[sp-1] = change[switch[sp-1]]     # 시작점 바꾸고
        s, e = sp-2, sp                         # 앞과 뒤의 idx가 스위치 범위이고 같으면
        while 0 <= s and e < N and switch[s] == switch[e]:
            switch[s] = change[switch[s]]
            switch[e] = change[switch[e]]
            s -= 1
            e += 1

# 한 줄에 20개씩 출력
for i in range(0, len(switch), 20):
    print(*switch[i:i+20])
