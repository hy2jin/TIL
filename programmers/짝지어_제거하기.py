def solution(s):
    L = len(s)
    if L%2: return 0
    
    stack = []
    for i in range(L):
        if not stack:
            stack.append(s[i])
        elif s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])

    if len(stack): return 0
    else: return 1