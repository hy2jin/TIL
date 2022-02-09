# BOJ 1316 그룹 단어 체커
import sys
sys.stdin = open('input.txt')

def isGroupWord(word, chk):
    for i in range(len(word)-1):
        if word[i] not in chk:
            return False
        if word[i] != word[i+1]:
            chk.remove(word[i])
    if word[-1] not in chk:
        return False
    return True


N = int(input())
cnt = 0
for _ in range(N):
    ip = input()
    ipSet = set(ip)
    if len(ip) == len(ipSet):
        cnt += 1
    elif isGroupWord(ip, ipSet):
        cnt += 1
print(cnt)
