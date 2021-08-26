# BOJ 2527 직사각형
def sq(sq1, sq2):
    a, b, c, d = sq1
    x, y, p, q = sq2
    if p < a or c < x or q < b or d < y:
        return 'd'
    if (a, b) == (p, q) or (c, b) == (x, q) or (a, d) == (p, y) or (c, d) == (x, y):
        return 'c'
    if p == a or c == x or q == b or d == y:
        return 'b'
    return 'a'


for _ in range(4):
    tmp = list(map(int, input().split()))
    sq1, sq2 = tmp[:4], tmp[4:]
    ans = sq(sq1, sq2)
    print(ans)
