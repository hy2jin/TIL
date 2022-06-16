from collections import deque
def solution(skill, skill_trees):
    ans = 0
    
    def check(word):
        Q = deque(list(skill))
        for w in word:
            if w not in skill:
                continue
            if len(Q) == 0:
                return 1
            if w != Q[0]:
                return 0
            Q.popleft()
        return 1
    
    for word in skill_trees:
        ans += check(word)
    return ans


def solution(skill, skill_trees):
    ans = 0
    for word in skill_trees:
        lst = list(skill)
        for w in word:
            if w in skill and w != lst.pop(0):
                break
        else:
            ans += 1
    return ans