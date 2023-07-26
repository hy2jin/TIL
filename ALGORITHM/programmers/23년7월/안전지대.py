# https://school.programmers.co.kr/learn/courses/30/lessons/120866

def solution(board):
    N = len(board)
    DIR = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1) ,(1, 0), (1, -1), (0, -1)]
    for i in range(N):
        for j in range(N):
            if board[i][j] != 1: continue
            for di, dj in DIR:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:
                    board[ni][nj] = 2
    ans = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                ans += 1
    return ans
