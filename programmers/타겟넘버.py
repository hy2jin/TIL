ans = 0
def solution(numbers, target):

    def DFS(i, v, L, target):
        global ans
        if i == L:
            if v == target:
                ans += 1
            return
        DFS(i+1, v + numbers[i], L, target)
        DFS(i+1, v - numbers[i], L, target)
    
    DFS(1, numbers[0], len(numbers), target)
    DFS(1, -numbers[0], len(numbers), target)
    return ans