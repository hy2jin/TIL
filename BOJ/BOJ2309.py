# BOJ 2309 일곱난쟁이
nine = [int(input()) for _ in range(9)]
find = False
for i in range(8):
    for j in range(i+1, 9):
        tmp = nine[:i] + nine[i+1:j] + nine[j+1:]
        if sum(tmp) == 100:
            find = True
            break
    if find: break
tmp.sort()
for k in tmp:
    print(k)
