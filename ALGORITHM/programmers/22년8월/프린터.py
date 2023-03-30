from collections import deque

def solution(priorities, location):
    lst = [(i, n) for i, n in enumerate(priorities)]
    Q = deque(lst)
    ans = 0

    while Q:
        idx, num = Q.popleft()
        if Q:
            m = max(Q, key = lambda x:x[1])     # 리스트의 두번째 원소를 기준으로 최대값을 구한다
            if num < m[1]:
                Q.append((idx, num))
            else:
                ans += 1
                if idx == location:
                    return ans
        else:
            return ans+1