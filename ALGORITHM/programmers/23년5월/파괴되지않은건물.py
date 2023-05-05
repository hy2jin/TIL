# 2차원 배열 누적합
def solution(board, skill):
    N, M = len(board), len(board[0])
    # 누적합 기록을 위한 배열
    arr = [[0] * (M + 1) for _ in range(N + 1)]
    
    # 누적합 기록, 부호 주의!
    for ty, r1, c1, r2, c2, degree in skill:
        arr[r1][c1] += degree if ty == 2 else -degree
        arr[r1][c2 + 1] += -degree if ty == 2 else degree
        arr[r2 + 1][c1] += -degree if ty == 2 else degree
        arr[r2 + 1][c2 + 1] += degree if ty == 2 else -degree
    
    # 행 기준 누적합, 열 기준 누적합
    for r in range(N):
        for c in range(M):
            arr[r][c + 1] += arr[r][c]
    for c in range(M):
        for r in range(N):
            arr[r + 1][c] += arr[r][c]
    
    ans = 0
    # 기존 배열과 더해주기
    for r in range(N):
        for c in range(M):
            board[r][c] += arr[r][c]
            if board[r][c] > 0: ans += 1
    return ans


# # 정확성 테스트 PASS, 효율성 테스트 FAIL
# # N최대 1000, M최대 1000, skill길이 250000 => 250,000,000,000 (2천5백억) 시간초과...
# def solution(board, skill):
#     ans = len(board) * len(board[0])
#     for ty, r1, c1, r2, c2, degree in skill:
#         if ty == 1: degree = -degree
#         for r in range(r1, r2 + 1):
#             for c in range(c1, c2 + 1):
#                 oldV = board[r][c]
#                 board[r][c] = oldV + degree
#                 if ty == 1 and oldV > 0 and board[r][c] <= 0:
#                     ans -= 1
#                 elif ty == 2 and oldV <= 0 and board[r][c] > 0:
#                     ans += 1
#     return ans