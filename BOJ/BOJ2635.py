# BOJ 2635 수 이어가기

N = int(input())
max_lst = []
max_len = 0

for i in range(N+1):
    lst = [N, i]
    j = 2
    while lst[j-2] - lst[j-1] >= 0:
        lst.append(lst[j-2] - lst[j-1])
        j += 1
    if j > max_len:
        max_lst = lst
        max_len = j
print(max_len)
print(*max_lst)