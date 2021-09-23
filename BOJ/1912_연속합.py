# BOJ 1912 연속합
import sys
sys.stdin = open('input.txt')
I = sys.stdin.readline
N = int(I())
number = list(map(int, I().split()))
ans = max(number)
if ans <= 0:
    print(ans)
    exit()

s = 0
for num in number:
    s += num
    if s < 0:
        s = 0
    elif ans < s:
        ans = s
print(ans)