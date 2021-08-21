# BOJ 2605 줄 세우기
N = int(input())
M = list(map(int,input().split()))

stack = [1]

for j in range(1,N):
    check = []
    for i in range(M[j]):
        check.append(stack.pop())

    stack.append(j+1)
    stack += check[::-1]

print(*stack)