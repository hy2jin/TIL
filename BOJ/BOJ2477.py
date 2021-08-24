# BOJ 2477 참외밭

N = int(input())
length = []
for i in range(6):
    d, l = map(int, input().split())
    length.append(l)
Area = 0
for j in range(6):
    tmp = length[j] * length[(j+1)%6]
    if tmp > Area:
        Area = tmp
        idx = j
area = length[(idx+3)%6] * length[(idx+4)%6]
print((Area - area) * N)
