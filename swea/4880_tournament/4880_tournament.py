import sys
sys.stdin = open('input.txt')


# 가위 바위 보 게임 / 승자의 idx 반환 / 비기면 작은 idx 반환
def game(l, r):
    if card[l] == card[r]:
        return l
    elif (card[l] == 1 and card[r] == 3) or (card[l] == 2 and card[r] == 1) or (card[l] == 3 and card[r] == 2):
        return l
    return r


def dfs(s, e):
    if s == e:
        return s
    left = dfs(s, (s+e)//2)         # 아직 더 쪼갤수 있으면? --> return s가 될때까지 재귀로 계속 들어감
    right = dfs((s+e)//2 + 1, e)
    return game(left, right)        # 만약에 하나여서 s값을 받아왔으면? --> 가위바위보 승자 반환


for tc in range(int(input())):
    N = int(input())
    card = list(map(int, input().split()))
    print('#{} {}'.format(tc+1, dfs(0, N-1) + 1))
