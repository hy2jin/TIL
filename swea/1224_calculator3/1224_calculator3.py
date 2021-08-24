import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    data = input()
    stack = []          # 우선순위 확인
    postfix = ''        # 후위표기법 담을 변수

    # 후위표기법으로 바꾸기
    for d in data:
        if d.isdigit():                 # 숫자면 후위표기식에 그대로 넣어줌
            postfix += d
        elif d == '(' or not stack:     # 여는 괄호거나 stack이 비어있으면 stack에 넣어줌
            stack.append(d)

        elif d == '*':        # * 보다 우선순위가 높은건 없고, 같은건 *
            while stack and stack[-1] == '*':
                postfix += stack.pop()
            stack.append(d)

        elif d == '+':      # + 보다 우선순위가 높거나 같은건 *, + ==> ( 를 제외하고 전부 pop
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(d)

        elif d == ')':      # 닫는 괄호는 버림 / 여는 괄호가 나올때까지 모두 pop()
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()     # 닫는 괄호와 짝인 여는 괄호도 버림

    while stack:                # 숫자가 끝났어도 stack에 연산자가 있을 수 있음
        postfix += stack.pop()  # 남은 연산자 하나씩 pop

    # 후위표기법 계산하기
    for p in postfix:
        if p.isdigit():         # 숫자
            stack.append(int(p))
        else:                   # 연산자
            b = stack.pop()
            a = stack.pop()
            if p == '+':
                stack.append(a + b)
            elif p == '*':
                stack.append(a * b)

    print('#{} {}'.format(tc, *stack))
