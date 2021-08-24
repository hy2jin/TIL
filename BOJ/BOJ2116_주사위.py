# BOJ 2116 주사위 쌓기
'''
옆면에 6이나 5가 와야함
'''
idx_pair = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}


def Dice_U(B, dice):            # 바닥에 있는 숫자와 주사위
    b = dice.index(B)           # B가 있는 idx
    return dice[idx_pair[b]]    # 위에 있는 숫자


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
six_idx = data[0].index(6)
