N = int(input())
TP = [tuple(map(int, input().split())) for _ in range(N)]

pay = [0] * 20
for i in range(N-1, -1, -1):
    if i + TP[i][0] > N:
        pay[i] = pay[i+1]
    else:
        pay[i] = max(pay[i+1], TP[i][1] + pay[TP[i][0] + i])

print(max(pay))