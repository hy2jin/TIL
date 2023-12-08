N, X = map(int, input().split())
T = list(map(int, input().split()))

i = 0
while True:
    if T[i] < X:
        break
    X += 1
    i = (i + 1) % N

print(i + 1)