# BOJ 10816 숫자 카드 2
import sys
sys.stdin = open('input.txt')

N = int(input())
cards = input().split()
dic = {}
for card in cards:
    try: dic[card] += 1
    except: dic[card] = 1
M = int(input())
chk = input().split()
ans = []
for c in chk:
    try: ans.append(dic[c])
    except: ans.append(0)
print(*ans)
