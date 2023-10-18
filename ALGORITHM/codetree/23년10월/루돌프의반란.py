import sys
sys.stdin = open('input.txt')

N, M, P, C, D = map(int, input().split())
arr = [[0] * N for _ in range(N)]
loc = [[0, 0] for _ in range(P + 1)]

CR, CC = map(int, input().split())
arr[CR][CC] = -1

for _ in range(P):
    n, r, c = map(int, input().split())
    loc[n] = (r - 1, c - 1)
    arr[r - 1][c - 1] = n

score   = [0] * (P + 1)
out     = [0] * (P + 1)
sleep   = [0] * (P + 1)

direction8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
direction4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move_cow(cr, cc):
    min_distance = N * N * 3
    # 돌진 대상 선정
    candidate = []
    for n in range(1, P + 1):
        pr, pc = loc[n]
        dt = (cr - pr) ** 2 + (cc - pc) ** 2
        if dt < min_distance:
            min_distance = dt
            candidate = [[-pr, -pc, n]]
        elif dt == min_distance:
            candidate.append([-pr, -pc, n])
    candidate.sort()
    pr, pc, pn = candidate[0]
    # 돌진 방향 선정
    cow_direction = 0
    for d in range(8):
        ncr, ncc = cr + direction8[d][0], cc + direction8[d][1]
        if not (0 <= ncr < N and 0 <= ncc < N):
            continue
        dt = (ncr - pr) ** 2 + (ncc - pc) ** 2
        if dt < min_distance:
            cow_direction = d
            min_distance = dt
    # 돌진
    ncr, ncc = cr + direction8[cow_direction][0], cc + direction8[cow_direction][1]
    if arr[ncr][ncc] == 0:
        arr[cr][cc] = 0
        arr[ncr][ncc] = -1
        return ncr, ncc
    crush(cr, cc, ncr, ncc, cow_direction, 'cp')
    return ncr, ncc


def crush(r, c, nr, nc, crush_dir, flag):
    # 소 -> 사람 충돌
    if flag == 'cp':
        pn = arr[nr][nc]
        score[pn] += C
        sleep[pn] = sec
        pr, pc = nr + C * direction8[crush_dir][0], nc + C * direction8[crush_dir][1]
        if not (0 <= pr < N and 0 <= pc < N):
            out[pn] = sec
        elif arr[pr][pc] == 0:
            loc[pn] = [pr, pc]
            arr[pr][pc] = pn
        else:
            crush(nr, nc, pr, nc, crush_dir, 'pp')
        arr[r][c] = 0
        arr[nr][nc] = -1
        return
            
    # 사람 -> 사람 충돌
    elif flag == 'pp':
        a, b = arr[r][c], arr[nr][nc]
        b_nr, b_nc = nr + direction8[crush_dir][0], nc + direction8[crush_dir][1]
        if not (0 <= b_nr < N and 0 <= b_nc < N):
            out[b] = sec
        elif arr[b_nr][b_nc] == 0:
            loc[b] = [b_nr, b_nc]
            arr[b_nr][b_nc] = b_nc
        else:
            crush(nr, nc, b_nr, b_nc, crush_dir, 'pp')
        arr[r][c] = 0
        arr[nr][nc] = a
        return
    # 사람 -> 소 충돌
    elif flag == 'pc':
        pn = arr[r][c]
        score[pn] += D
        sleep[pn] = sec
        reverse_dir = (crush_dir + 2) % 4
        pr, pc = r + D * direction4[reverse_dir][0], c + D * direction4[reverse_dir][1]
        if not (0 <= pr < N and 0 <= pc < N):
            out[pn] = sec
        elif arr[pr][pc] == 0:
            loc[pn] = [pr, pc]
            arr[pr][pc] = pn
        else:
            arr[nr][nc] = pn
            crush(r, c, pr, nc, reverse_dir, 'pp')
            arr[nr][nc] = -1


def move_person(pr, pc):
    cow_dt = (CR - pr) ** 2 + (CC - pc) ** 2
    person_dir = -1
    for d in range(4):
        nr, nc = pr + direction4[d][0], pc + direction4[d][1]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if arr[nr][nc] > 0:
            continue
        dt = (CR - nr) ** 2 + (CC - nc) ** 2
        if dt < cow_dt:
            person_dir = d
            break
    if person_dir < 0:
        return
    nr, nc = pr + direction4[person_dir][0], pc + direction4[person_dir][1]
    if arr[nr][nc] == 0:
        pn = arr[pr][nc]
        arr[pr][pc] = 0
        loc[pn] = [nr, nc]
        arr[nr][nc] = pn
    crush(pr, pc, nr, nc, person_dir, 'pc')
        

for sec in range(1, M + 1):
    CR, CC = move_cow(CR, CC)
    for num in range(1, P + 1):
        if out[num]:
            continue
        if sleep[num] and sleep[num] + 2 > sec:
            continue
        move_person(loc[num][0], loc[num][1])
    
    for num in range(1, P + 1):
        if out[num] == 0:
            score[num] += 1
    
    if sum(out) == P:
        break

print(*score[1:])