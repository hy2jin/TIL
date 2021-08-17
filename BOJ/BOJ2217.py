# BOJ 2217 로프
N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

def compare():
    global rope
    n = len(rope)
    min_v = min(rope) * n
    rope.remove(min(rope))
    next_min = min(rope) * (n-1)
    return max(min_v, next_min)

while len(rope) > 2:
    min_v = min(rope) * len(rope)
    if min_v == compare():
        break

