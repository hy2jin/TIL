# BOJ 16953 A → B
from collections import deque

A, B = map(int, input().split())
Q = deque()
Q.append((A, 1))

while Q:
    num, cnt = Q.popleft()
    if num == B:
        print(cnt)
        exit()
    if num * 2 <= B:
        Q.append((num*2, cnt+1))
    tmp = int(str(num) + '1')
    if tmp <= B:
        Q.append((tmp, cnt+1))
print(-1)