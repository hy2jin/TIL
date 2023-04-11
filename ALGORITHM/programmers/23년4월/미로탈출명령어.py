def solution(n, m, x, y, r, c, k):
    dis = abs(x - r) + abs(y - c)
    more = k - dis
    if more < 0: return 'impossible'
    if more % 2: return 'impossible'

    dCnt = uCnt = 0             # 각 방향으로 몇 칸 가야하는지
    lCnt = rCnt = 0
    if x < r: dCnt = r - x      # 아래로
    else: uCnt = x - r          # 위로
    if y < c: rCnt = c - y      # 오른쪽으로
    else: lCnt = y - c          # 왼쪽으로

    dMore = min(n - max(x, r), more//2)     # 상하로 몇칸 더?
    more -= (dMore * 2)         # 총 남은 칸 수

    lMore = min(min(y, c) - 1, more//2)     # 좌우로 몇칸 더?
    more -= (lMore * 2)         # 총 남은 칸 수

    dStr = 'd' * (dCnt + dMore)
    lStr = 'l' * (lCnt + lMore)
    center = 'rl' * (more//2)   # 남은 칸이 있으면 그건 오왼으로 움직이는게 좋다
    rStr = 'r' * (rCnt + lMore)
    uStr = 'u' * (uCnt + dMore)

    return dStr + lStr + center + rStr + uStr


print(solution(3, 4, 2, 3, 3, 1, 5))       # dllrl
print(solution(2, 2, 1, 1, 2, 2, 2))       # dr
print(solution(3, 3, 1, 2, 3, 3, 4))       # impossible



# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

# dx = [1, 0, 0, -1]
# dy = [0, -1, 1, 0]
# dAlpha = ['d', 'l', 'r', 'u']
# answer = "z"


# def isVaild(nx, ny, n, m):
#     return 1 <= nx and nx <= n and 1 <= ny and ny <= m


# def dfs(n, m, x, y, r, c, prev_s, cnt, k):
#     global answer
#     if k < cnt + abs(x - r) + abs(y - c):
#         return
#     if x == r and y == c and cnt == k:
#         answer = prev_s
#         return
#     for i in range(4):
#         if isVaild(x + dx[i], y + dy[i], n, m) and prev_s < answer:
#             dfs(n, m, x + dx[i], y + dy[i], r, c, prev_s+dAlpha[i], cnt + 1, k)


# def solution(n, m, x, y, r, c, k):
#     dist = abs(x - r) + abs(y - c)
#     if dist > k or (k - dist) % 2 == 1:
#         return "impossible"

#     dfs(n, m, x, y, r, c, "", 0, k)

#     return answer