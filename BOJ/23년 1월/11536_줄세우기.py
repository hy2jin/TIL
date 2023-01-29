N = int(input())
order = [0, 0]
prev = input()
for _ in range(N - 1):
    now = input()
    if prev < now:
        order[0] += 1
    else:
        order[1] += 1
    prev = now

if order[0] == N - 1:
    ans = 'INCREASING'
elif order[1] == N - 1:
    ans = 'DECREASING'
else:
    ans = 'NEITHER'

print(ans)
