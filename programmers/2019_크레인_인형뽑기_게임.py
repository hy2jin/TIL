def solution(board, moves):
    
    def bomb(lst):
        L = len(lst)
        if L == 1:
            return lst, 0
        if lst[L-1] == lst [L-2]:
            return lst[:L-2], 2
        return lst, 0

    lst = []
    N = len(board)
    ans = 0

    for i in moves:
        c = i - 1
        for n in range(N):
            if board[n][c]:
                lst.append(board[n][c])
                board[n][c] = 0
                lst, cnt = bomb(lst)
                ans += cnt
                break
    return ans
