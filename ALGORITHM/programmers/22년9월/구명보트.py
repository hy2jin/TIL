from collections import deque

def solution(people, limit):
    ans = 0
    Q = deque(sorted(people))
    while Q:
        p = Q.pop()
        if Q and p + Q[0] <= limit:
            Q.popleft()
        ans += 1
    return ans

def solution2(people, limit):
    people.sort()
    i = 0
    j = len(people) - 1
    while i < j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return len(people) - i