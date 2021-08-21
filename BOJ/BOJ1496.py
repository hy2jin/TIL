# BOJ 1496 딱지놀이

def play(A, B):
    for pic in (4, 3, 2, 1):
        a, b = A.count(pic), B.count(pic)
        if a > b: return 'A'
        elif a < b: return 'B'
    return 'D'

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N*2)]
i = 0
while i < N*2:
    A, B = AB[i][1:], AB[i+1][1:]
    i += 2
    print(play(A, B))
