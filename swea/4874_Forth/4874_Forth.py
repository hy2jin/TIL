import sys
sys.stdin = open('input.txt')
for tc in range(int(input())):
    postfix = input().split()
    stack = []
    for p in postfix:
        if p not in '*/+-.':    # 숫자
            stack.append(p)

        elif p in '*/+-':       # 사칙연산
            try:
                b = int(stack.pop())
                a = int(stack.pop())
                if p == '*':
                    stack.append(a * b)
                elif p == '/':
                    stack.append(a // b)
                elif p == '+':
                    stack.append(a + b)
                elif p == '-':
                    stack.append(a - b)
            except:             # stack에 하나만 있었다면?
                ans = 'error'
                break

        elif p == '.':          # 마지막 연산자
            ans = stack.pop()
            # 만약 끝난게 아니라면? stack이 비어있지 않으면?
            if stack:
                ans = 'error'

    print('#{} {}'.format(tc+1, ans))
