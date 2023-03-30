# BOJ 2920 음계

ip = input()
ans = 'mixed'
if ip == '1 2 3 4 5 6 7 8':
    ans = 'ascending'
elif ip == '8 7 6 5 4 3 2 1':
    ans = 'descending'
print(ans)