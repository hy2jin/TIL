from collections import deque

def solution(prices):
    Q = deque(prices)
    ans = []
    
    while Q:
        price = Q.popleft()
        sec = 0
        for p in Q:
            sec += 1
            if price > p: break
        ans.append(sec)
    return ans
