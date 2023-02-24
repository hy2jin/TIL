def calc(string):
    lst = list(map(int, string.split('+')))
    return sum(lst)

string = input()
lst = string.split('-')

ans = 0
for i in range(len(lst)):
    if i == 0:
        ans += calc(lst[i])
    else:
        ans -= calc(lst[i])
print(ans)
