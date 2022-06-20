N = int(input())
# lst = [0, 1]
# for i in range(2, N+1):
#     lst.append(lst[i-2] + lst[i-1])
# print(lst[N])

if N == 1:
    print(1)
else:
    a, b = 0, 1
    for _ in range(N):
        a, b = b, a+b
    print(a)